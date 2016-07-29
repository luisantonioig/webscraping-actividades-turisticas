#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import html
import requests

# Luis Antonio Ibarra
#27-07-2016
# funcion para obtener el contenido de una página web cómo árbol xml
# devuelve un arbol xml
def getTreeContent():
	#page = requests.get('https://www.tripadvisor.com.mx/Attractions-g445056-Activities-Sayulita_Pacific_Coast.html')
        #page = requests.get('http://www.visitmexico.com/es/zacatecas-mexico')
        page = requests.get('http://agendaculturalzacatecas.com/')
	tree = html.fromstring(page.content)
	return tree
# Fin getPageContent

# Luis Antonio Ibarra
#27-07-2016
# funcion para obtener el textp de una árbol xml cómo arreglo de string
#devuelve un arreglo con los string
def getTextTree(tree):
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
	#Obtenemos el texto de las etiquetas p
	p = tree.xpath("//p/text()")
	while "\n" in p:
	  p.remove('\n')
	while " " in p:
	  p.remove(" ")
	lista = lista + p
	#Obtenemos el texto de las etiquetas span
	span = tree.xpath("//span/text()")
	while "\n" in span:
	  span.remove("\n")
	while " " in span:
	  span.remove(" ")
	lista = lista + span
	temp_list = list()
	for elemento in lista:
	  temp_list.append(elemento.encode("utf8"))
	lista = temp_list
	return lista
# Fin getTextTree
