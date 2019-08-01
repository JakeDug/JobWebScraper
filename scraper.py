# -*- coding: utf-8 -*-
# import libraries
import urllib2
from bs4 import BeautifulSoup
import csv
from datetime import datetime

### INDEED ###

web_page = 'https://ie.indeed.com/software-developer-jobs'

# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(web_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

title_list = []
info_list = []
url_list = []

divs = soup.findAll(class_= 'title')    
for div in divs:

	title_box = div.find()
	title = title_box.text.strip()
	title_list.append(title)
	for a in div.find_all('a', href=True):
		url_list.append('http://ie.indeed.com' + str(a['href']))

divs = soup.findAll(class_= 'sjcl')    
for div in divs:

	info_box = div.find()
	info = info_box.text.strip()
	info_list.append(info)

### IRISH JOBS ###

web_page = 'https://www.irishjobs.ie/ShowResults.aspx?Keywords=Graduate+Software+Developer&SortBy=Relevance&PerPage=100'

# query the website and return the html to the variable ‘page’
page = urllib2.urlopen(web_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

divs = soup.findAll(class_= 'job-result-title')    
for div in divs:
	title_box = div.find()
	title = title_box.text.strip()
	title_list.append(title)
	for a in div.find_all('a', href=True):
		url_list.append('https://irishjobs.ie' + str(a['href']))
		

divs = soup.findAll(class_= 'job-result-overview')    
for div in divs:

	info_box = div.find()
	info = info_box.text.strip()
	info_list.append(info)


with open('index.csv', 'a') as csv_file:
	i = 0
	while i < len(title_list):
		 writer = csv.writer(csv_file)
		 writer.writerow([title_list[i].encode('ascii', 'ignore'), info_list[i].encode('ascii', 'ignore'), url_list[i].encode('ascii', 'ignore'), datetime.now()])
		 i+=1
