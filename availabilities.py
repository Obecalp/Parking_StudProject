#!/usr/bin/python3
import sys
import json

checklist=[] #sert à renvoyer un rapport d'erreur spécifique si aucun parking n'a été trouvé
if len(sys.argv) != 3:
	print("./availabilities.py <fichier de disponibilités> <bornemin> avec <fichier de disponibilités> le chemin vers le fichier JSON de places libres et <bornemin> la limite minimum de places libres pour retourner \033[31ml'identifiant\033[0m d'un parking", file=sys.stderr)
	exit(2)
try:
	data=open(sys.argv[1])
	dispo = json.load(data)
except IOError:
	exit (4)

try:
	for line in dispo:
		if int(line['fields']['disponibilite']) > int(sys.argv[2]):
			print(line['fields']['idobj'])
			checklist.append(line['fields']['idobj'])
except ValueError:
	exit (6)
if len(checklist) == 0:
	exit (5)
