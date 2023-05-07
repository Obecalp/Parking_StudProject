#!/bin/bash


#testerreur chercher l'erreur $2 après l'exécution d'un programme et délivre le message en $3 si la condition est vérifiée, puis renvoit le code d'erreur en $4
function testerreur(){
	if [ $1 = $2 ];then
		echo $3 1>&2
		exit $4
	fi
	}

#datation: verifie l'existence d'un fichier en entree 1 et sa datation en fonction de l'entrée 2 (-mtime +10 par ex), et télécharge le lien en entrée 3 s'il n'existe pas ou ne correspond pas aux critères de temps, message et exit en cas d'échec
function datation(){

	if [ -e $1 ];then
		if [ "$(find $1 $2)" = "$1" ];then
			wget -O $1 $3
		fi
	else 
		wget -O $1 $3
	fi
}

#Coordo: permet d'entrer les valeurs données par adresscoord.py dans jemegare.py sous forme de 2 arguments: position1,position2
function Coordo(){
	position1=$(echo $1 | cut -d ' ' -f1)
	position2=$(echo $1 | cut -d ' ' -f2)
	}


Dossiercible=~/.jemegare

if [ $# != 4 ]; then
	echo "mauvais nombre de paramètres, exécution: ./jemegare.sh <adresse> <entier=durée stationnement> <entier=places mini> <entier=taille de la liste>" 1>&2
	exit 1
fi

#Changer la valeur de la variable Dossier cible permet de changer facilement le dossier dans lequel seront stockés les fichier .json		

if [ ! -e $Dossiercible ];then
	mkdir $Dossiercible
	echo "Dossier $Dossiercible créé"
fi

# La datation de adresses.json et distance.y a été prise au minimum (0) pour éviter le re-téléchargement si ils sont présents, et pour pouvoir les inclure dans la fonction
datation "$Dossiercible/disponibilites.json" "-mmin +60" "https://data.nantesmetropole.fr/explore/dataset/244400404_parkings-publics-nantes-disponibilites/download/?format=json&timezone=Europe/Berlin&lang=fr"
datation "$Dossiercible/tarifs.json" "-mtime +30" "https://data.nantesmetropole.fr/explore/dataset/244400404_parkings-publics-nantes-tarification-horaire/download/?format=json&timezone=Europe/Berlin&lang=fr"
datation "$Dossiercible/adresses.json" "-mmin -0" "https://data.nantesmetropole.fr/explore/dataset/244400404_adresses-postales-nantes-metropole/download/?format=json&timezone=Europe/Berlin&lang=fr"
datation "distance.py" "-mmin -0" "https://madoc.univ-nantes.fr/mod/resource/view.php?id=1556908"

#test des exécutions de addresscoord.py et availibilities.py
position=$(./addresscoord.py "$Dossiercible/adresses.json" "$1")
erreur1=$?
testerreur $erreur1 3 "l'adresse $1 n'a pas été trouvée" 6
testerreur $erreur1 4 "Erreur dans l'ouverture du fichier $Dossiercible/adresses.json" 4


testdispo=$(./availabilities.py "$Dossiercible/disponibilites.json" "$3")
erreur2=$?
testerreur $erreur2 4 "Erreur dans l'ouverture du fichier $Dossiercible/disponibilites.json" 4
testerreur $erreur2 5 "Aucun parking ne dispose actuellement d'au moins $3 places dans la liste $Dossiercible/disponibilites.json" 5
testerreur $erreur2 6 "Erreur dans la saisie du nombre de places, veuillez entrer ./jemegare.sh <adresse> <entier=durée stationnement> <entier=places mini> <entier=taille de la liste>" 6


Coordo "$position"

if ! [[ $4 =~ ^[0-9]+$ ]];then
	echo "Erreur dans la saisie de la taille de la liste, veuillez entrer ./jemegare.sh <adresse> <entier=durée stationnement> <entier=places mini> <entier=taille de la liste>"
	exit 6
fi
./availabilities.py "$Dossiercible/disponibilites.json" "$3" | ./jemegare.py "$Dossiercible/tarifs.json" $position1 $position2 "$2" | head -$4
