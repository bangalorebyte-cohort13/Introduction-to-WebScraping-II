#!/usr/bin/env python3.6

from bs4 import BeautifulSoup
import requests
import csv
import datetime

url = 'http://quotes.wsj.com/'
company_list = ["AMZN","AAPL","NFLX","MSFT"]
full_url_list = []
data_list = []

for i in range(len(company_list)):
	full_url = url + company_list[i]
	full_url_list.append(full_url)
#print(full_url_list)

with open('stocks_7.csv', 'w', newline='') as outfile:
	column_names = ["Stock_Name","Current_Price","Timestamp","Opening_Price","Closing_Price","Price_Change"]
	writer = csv.writer(outfile)
	writer.writerow(column_names)
	for i in full_url_list:
		page = requests.get(i)
		html = page.content
		s = BeautifulSoup(html,"html.parser")
		current_price = s.find(id='quote_val').text
		opening_closing_price = s.findAll("ul",attrs={"class": "cr_data_collection"})
		print(opening_closing_price)
		text = (opening_closing_price[1]).text
		#print(text)
		details_list = text.split()
		open_price = details_list[1]
		close_price = details_list[4]
		price_change = s.find("span",attrs = {"id":"ms_quote_changePer"}).text
		data_list = [i[len(url):],current_price, datetime.datetime.time(datetime.datetime.now()), open_price, close_price,price_change]
		#print(data_list)
		writer.writerow(data_list)




