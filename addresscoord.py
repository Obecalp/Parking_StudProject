#!/usr/bin/python3
import sys
import json


if len(sys.argv) != 3:
	print("Mauvais nombre de paramètres: Veuillez utiliser la liste d'adresses mise à disposition, puis une adresse entre guillements telle que: 31 Bis = 31B", file= sys.stderr)
	exit(1)

try:
	data=open(sys.argv[1])
	adresse=json.load(data)
	x= sys.argv[2]
except IOError: #En cas de fichier incorrect, code erreur pour l'exécution de testerreur du programme
	exit(4)

for line in adresse:
	if line['fields']['adresse'].upper()== x.upper():
		print(line['fields']['geo_shape']['coordinates'][0],line['fields']['geo_shape']['coordinates'][1])
		exit(0)
exit(3)


