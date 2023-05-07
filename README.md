Ceci est mon premier language de script avec pour objectif la mise en oeuvre des connaissances acquises en Python. Il a en réalité essentiellement servi à apprendre le Python et est le reflet de mes connaissances en bash/Python au premier semestre exclusivement. L'idée du projet et de sa structure (le rôle de chaque fichier) sont l'oeuvre de l'enseignant Frederic Goualard. Il n'a été cependant donné aucune instruction de programmation/algorithmique, ce domaine était libre.

Ce programme a pour objectif de permettre à l'utilisateur de localiser, à partir d'une adresse située sur Nantes, les parking les plus proches avec leur tarifs, et permettre à l'utilisateur de choisir le nombre de places minimum disponibles qu'ils souhaite.
Il doit être utilisé à partir d'un terminal linux par la commande:
./jemegare.sh <adresse> <entier=durée stationnement> <entier=places minimum du parking> <entier=taille de la liste de parking>

En fonction de ses instructions l'utilisateur verra affiché sur le terminal une liste de parking en commençant par le plus proche de sa position, avec le prix attendu en fonction du temps qu'il souhaite rester.

La liste des tarifs des parkings est mis à jour tout les 30 jour, la liste des places disponibles est mise à jour toutes les heures à partir du site https://data.nantesmetropole.fr/pages/home/

