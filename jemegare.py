#!/usr/bin/python3

import sys
import json
import datetime
import distance

date = int(datetime.datetime.now().hour)
listeidentifiant=[]
try:
	data=open(sys.argv[1])
	dico=json.load(data)
except IOError:
	print("Erreur dans l'ouverture du fichier", sys.argv[1], file=sys.stderr)
	exit (4)
try:
	lat1=float(sys.argv[2])
	lon1=float(sys.argv[3])

	duree=int(sys.argv[4])

except ValueError:
	print("Erreur dans la saisie de la durée, veuillez entrer ./jemegare.sh <'adresse'> <entier=durée stationnement> <entier=places mini> <entier=taille de la liste>")
	exit (6)

#Dictionnaire contenant les tarifs en fonction des parkings
dicotarif={}
#Listedistances pourra être triée pour ressortir les valeurs en fonction de la distance à parcourir.
listedistances=[]

# Fonction pour retourner le prix souhaité en fonction des tarifs stockés dans tarifJ/tarifN, de la tranche horaire (datation) et de la duree souhaitée (duration)
def calcultarif(tarifJ,tarifN,datation,duration):
	if datation > 8 and datation <= 19:
		for tupltarif in tarifJ:
			if duration < tupltarif[1]:
				return tupltarif[0]
		return tarifJ[-1][0]
	else:
		for tupltarif in tarifN:
			if duration < tupltarif[1]:
				return tupltarif[0]
		return tarifN[-1][0]

#Listage des identifiants
for entree in sys.stdin:
	listeidentifiant.append(int(entree))

for identifiant in listeidentifiant:
	for line in dico:
		if str(line['fields']['idobj']) == str(identifiant):
			distancy= float(distance.distance(line['fields']['location'][1],line['fields']['location'][0],lat1,lon1))
			listedistances.append((distancy, line['fields']['idobj'])) #création de la liste servant à trier les distances
			
			try:
				tarifjour=[(line['fields']['10min'], 10), (line['fields']['20min'], 20), (line['fields']['30min'], 30), (line['fields']['40min'], 40), (line['fields']['50min'], 50), (line['fields']['1h'], 60), (line['fields']['1h30'], 90), (line['fields']['2h'], 120), (line['fields']['2h30'], 150), (line['fields']['3h'], 180), (line['fields']['11h'], 660)]
				tarifnuit=[(line['fields']['nuit_10min'], 10), (line['fields']['nuit_20min'], 20), (line['fields']['nuit_30min'], 30), (line['fields']['nuit_40min'], 40), (line['fields']['nuit_50min'], 50), (line['fields']['nuit_1h'], 60), (line['fields']['nuit_1h30'], 90), (line['fields']['nuit_2h'], 120), (line['fields']['nuit_2h30'], 150), (line['fields']['nuit_3h_et'], 180)]


			except KeyError:
				tarifnuit=[("0.0", 10)]
				pass #permet d'éviter un arrêt lors de la lecture des dictionnaires des parkings gratuit la nuit.


			tarif=calcultarif(tarifjour,tarifnuit,date,duree)
			dicotarif[line['fields']['idobj']]=tarif
listedistances.sort(key=lambda x:x[0]) #triage de la liste

for i in listedistances:
	for line in dico: 
		if line['fields']['idobj'] == i[1]:
			print(line['fields']['nom_du_parking'],":", dicotarif[line['fields']['idobj']],"€")
