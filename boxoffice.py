#!/usr/bin/env python3.6


from bs4 import BeautifulSoup
import requests
import csv

url = "http://www.boxofficemojo.com/studio/?view=company&view2=yearly&yr=20%02d&p=.htm"
rows = []
list_ = []

def pagination():
	for i in range(0,19):
		full_url = url % i
		list_.append(full_url)
	return list_ 


def soupify(x):
	for i in x:
		page = requests.get(i)
		html = page.content
		s = BeautifulSoup(html)
		table = s.find("table", attrs = {'cellpadding': '5'	})
		print(table)
		return table

def get_rows(x):
		for i in table.find_all('tr'):
			cells =[]
			for cell in i.find_all('td'):
				text = cell.text
				cells.append(text)
			rows.append(cells)	
		print(rows)

#print(pagination())
(soupify(pagination()))

outfile = open("./boxoffice5.csv", "w")
writer = csv.writer(outfile)
writer.writerows(rows)
	
	

