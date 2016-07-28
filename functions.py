# Saul Alonso Ibarra
# 28-07-2016
# funcion que recibe como parametro un array con expresiones
# y devuelve solo aquellas que contengan la palabra sayulita
def depureComments( comments ):
	sayulitacomments=[]
	for comment in comments:
		if 'sayulita' in comment:
			sayulitacomments.append(comment)
	return sayulitacomments
# Fin depureComments	

# Saul Alonso Ibarra
# 28-07-2016
# funcion que recibe como parametro un array con expresiones naturales
# y devuelve las actividades encontradas en las expresiones
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
	'excursion',
	'liberacion de tortugas',
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
	]
	sayulitaactivities=[]
	for comment in comments:
		for activity in activities:
			if activity in comment:
				sayulitaactivities.append(activity)
	return sayulitaactivities
# Fin serchActivities
