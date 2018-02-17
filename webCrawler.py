import sys
import requests
from lxml import html, etree

website = sys.argv[1]

#storing response
response = requests.get(website)
tree = html.fromstring(response.text)

alllinks = tree.xpath('.//a/@href')

for link in alllinks:
	print(link)