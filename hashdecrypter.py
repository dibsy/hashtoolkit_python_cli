#!/usr/bin/python
import httplib
from bs4 import BeautifulSoup
import requests
import sys

if len(sys.argv)!=2:
	print "usage : ./hashdecrypter.py 21232f297a57a5a743894a0e4a801fc3"
else:

	url = "http://hashtoolkit.com/reverse-hash?hash={}".format(sys.argv[1])
	request = requests.get(url)
	data = request.text
	soup = BeautifulSoup(data,'html.parser')

	table = soup.find('table')
	try: 
		table_rows = table.find_all('tr')

		for tr in table_rows:
			td = tr.find_all('td')
			row = [i.text.strip() for i in td]
			print str(row).encode('utf-8')
	except:
		print("No hash found for {}".format(sys.argv[1]))
