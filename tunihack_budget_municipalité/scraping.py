#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests
import lxml.html as lh
from urllib2 import urlopen
import pandas as pd
from bs4 import BeautifulSoup
import csv

URL = 'http://www.finances.gov.tn/applications/budget_collectivites/afficher_recette2015_modif.php'
payload = {
    'municipalite': '14013',
    'region': '14',
    'annee': '2018',
    'ok': 'المصادقة',
}

session = requests.session()
r = requests.post(URL, data=payload)
html = r.content
soup = BeautifulSoup(html, 'lxml') # Parse the HTML as a string
table = soup.find_all('table')[0] # Grab the first table
#print (table.encode("utf-8"))
headers = [th.text.encode("utf-8") for th in table.select("tr th")]

with open("out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow(headers)
    wr.writerows([[td.text.encode("utf-8") for td in row.find_all("td")] for row in table.select("tr + tr")])
