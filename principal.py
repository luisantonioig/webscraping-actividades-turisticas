from lxml import html
import requests

page = requests.get('https://www.tripadvisor.com.mx/Attractions-g445056-Activities-Sayulita_Pacific_Coast.html')
tree = html.fromstring(page.content)

divs = tree.xpath("//div/text()")
divs.remove('\n')
print divs[-3]
