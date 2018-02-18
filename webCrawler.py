import sys
import requests
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from lxml import html

website = sys.argv[1]

# render class
class Render(QWebEnginePage):
	def __init__(self, url):
		self.app = QApplication(sys.argv)
		QWebEnginePage.__init__(self)
		self.html = ''
		self.loadFinished.connect(self._loadFinished)
		self.load(QUrl(url))
		self.app.exec_()

	def _loadFinished(self, result):
		self.toHtml(self.Callable)
		print('Load finished')

	def Callable(self, html_str):
		self.html = html_str
		self.app.quit()
		

r = Render(website)

# storing response
response = r.html
formatted_result = str(response)
tree = html.fromstring(formatted_result)

# stroing all links
alllinks = tree.xpath('.//a/@href')

# filter all empty links
alllinks = [link for link in alllinks if not link == '#']

for link in alllinks:
	print(link)