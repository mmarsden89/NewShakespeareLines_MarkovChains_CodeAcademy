import urllib2 
from random import randint 
from bs4 import BeautifulSoup

num = randint(1,150)

old_poems = 'http://www.literaturepage.com/read/shakespeare_sonnets-%d.html' % (num)
old_poems2 = 'http://www.literaturepage.com/read/shakespeare_sonnets-%d.html' % (num)
def fetch_data():
	website = old_poems
	page = urllib2.urlopen(website)
	html_doc = page.read()
	soup = BeautifulSoup(html_doc, 'html.parser')
	textfetch = soup.find('p', attrs={'class':'readingpoetry'})
	newtext = textfetch.text
	website2 = old_poems2
	page2 = urllib2.urlopen(website)
	html_doc2 = page.read()
	soup2 = BeautifulSoup(html_doc, 'html.parser')
	textfetch2 = soup.find('p', attrs={'class':'readingpoetry'})
	newtext2 = textfetch2.text
	return newtext + newtext2
	
