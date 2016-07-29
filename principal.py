from lxml import html
import requests

page = requests.get('https://www.tripadvisor.com.mx/Attractions-g445056-Activities-Sayulita_Pacific_Coast.html')
tree = html.fromstring(page.content)

def eliminarAcentos(cadena):

    d = {
        '\xc1':'A',
        '\xc9':'E',
        '\xcd':'I',
        '\xd3':'O',
        '\xda':'U',
        '\xdc':'U',
        '\xd1':'N',
        '\xc7':'C',
        '\xed':'i',
        '\xf3':'o',
        '\xf1':'n',
        '\xe7':'c',
        '\xba':'',
        '\xb0':'',
        '\x3a':'',
        '\xe1':'a',
        '\xe2':'a',
        '\xe3':'a',
        '\xe4':'a',
        '\xe5':'a',
        '\xe8':'e',
        '\xe9':'e',
        '\xea':'e',        
        '\xeb':'e',        
       '\xec':'i',
        '\xed':'i',
        '\xee':'i',
        '\xef':'i',
        '\xf2':'o',
        '\xf3':'o',
        '\xf4':'o',    
        '\xf5':'o',
        '\xf0':'o',
        '\xf9':'u',
        '\xfa':'u',
        '\xfb':'u',                
        '\xfc':'u',
        '\xe5':'a'}
    nueva_cadena = cadena
    return nueva_cadena

#Lista en la que guardaremos el contenido de una pagina web
lista = list()

#Obtenemos el texto de las etiquetas div
divs = tree.xpath("//div/text()")
while "\n" in divs:
  divs.remove('\n')
while " " in divs:
  divs.remove(" ")
lista = lista + divs

#Obtenemos el texto de las etiquetas a
a = tree.xpath("//a/text()")
while "\n" in a:
  a.remove('\n')
while " " in a:
  a.remove(" ")
lista = lista + a

#Obtenemos el texto de las etiquetas spam
spam = tree.xpath("//spam/text()")
while "\n" in spam:
  spam.remove("\n")
while " " in spam:
  spam.remove(" ")
lista = lista + spam

temp_list = list()
for elemento in lista:
  temp_list.append(eliminarAcentos(elemento))
lista = temp_list

print lista[1]
