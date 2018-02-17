import sys
import requests
from lxml import html, etree

website = sys.argv[1]

# storing response
response = requests.get(website)
tree = html.fromstring(response.text)

# stroing all links
alllinks = tree.xpath('.//a/@href')

# filter all empty links
alllinks = [link for link in alllinks if not link == '#']

for link in alllinks:
	print(link)