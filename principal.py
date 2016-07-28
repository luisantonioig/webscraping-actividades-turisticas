from lxml import html
import requests

page = requests.get('https://www.tripadvisor.com.mx/Attractions-g445056-Activities-Sayulita_Pacific_Coast.html')
tree = html.fromstring(page.content)

#Obtenemos el texto de las etiquetas div
divs = tree.xpath("//div/text()")
while "\n" in divs:
  divs.remove('\n')
while " " in divs:
  divs.remove(" ")

#Obtenemos el texto de las etiquetas a
a = tree.xpath("//a/text()")
while "\n" in a:
  a.remove('\n')
while " " in a:
  a.remove(" ")

#Obtenemos el texto de las etiquetas spam
spam = tree.xpath("//a/text()")
while "\n" in spam:
  spam.remove("\n")
while " " in spam:
  spam.remove(" ")

print a
print divs
print spam
