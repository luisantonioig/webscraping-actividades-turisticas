#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Saúl Alonso Ibarra
#29-07-2016
#funcion que recibe un string y regresa el string sin acentos
import unicodedata
def elimina_acentos(st):
   return ''.join((c for c in unicodedata.normalize('NFD', st) if unicodedata.category(c) != 'Mn'))
 

# Saul Alonso Ibarra
# 28-07-2016
# funcion que recibe como parametro un array con expresiones y una palabara a buscar
# y devuelve solo aquellas que contengan la palabra a buscar
# 29-07-2016  Se da formato a las cadenas en minusculas y se eliminan acentos al comparar
def depureComments( comments,word ):
	sayulitacomments=[]
	for comment in comments:
		word=word.lower()
		comment=comment.lower()
		if elimina_acentos(word.decode('utf8')) in elimina_acentos(comment.decode('utf8')):
			sayulitacomments.append(comment)
	return sayulitacomments
# Fin depureComments	

# Saul Alonso Ibarra
# 28-07-2016
# funcion que recibe como parametro un array con expresiones naturales
# y devuelve las actividades encontradas en las expresiones
# 29-07-2016  Se da formato a las cadenas en minusculas y se eliminan acentos al comparar
def serchActivities( comments ):
	 # Catalogo de todas las actividades turisticas encontradas
	activities=[
	'avistamiento de aves',
	'buceo',
	'bucear',
	'cabalgata',
	'cabalgar',
	'canonismo',
	'caminata',
	'ciclismo',
	'escalada',
	'escalar',
	'expediciones',
	'explorar',
	'excursión',
	'liberación de tortugas',
	'natacion',
	'manejar',
	'conducir',
	'tirolesa',
	'globo aerostatico',
	'golf',
	'kayak',
	'paracaidismo',
	'parapente',
	'rafting',
	'rappel',
	'recoridos',
	'recorrer',
	'surf',
	'tours',
	'ascenso',
	'paseos',
	'pesca',
	'pescar',
	'yoga',
	'nadar',
	'bird watching',
        'recorrido',
        'Callejoneadas',
]
	sayulitaactivities=[]
	for comment in comments:
		for activity in activities:
			activity=activity.lower()
			comment=comment.lower()
			if elimina_acentos(activity.decode('utf8')) in elimina_acentos(comment.decode('utf8')):
				sayulitaactivities.append(activity)
	return sayulitaactivities
# Fin serchActivities
