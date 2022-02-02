from turtle import distance
from bs4 import BeautifulSoup as bs
import time 
import pandas as pd
import requests

start_url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(start_url)
soup = bs(page.text , 'html.parser')
star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr')

temp_list = []

time.sleep(10)

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_name = []
distance = []
mass = []
radius = []
consti = []
year = []

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][0][:-5])
    distance.append(temp_list[i][5])
    radius.append(temp_list[i][8])
    mass.append(temp_list[i][7])
    consti.append(temp_list[i][1])
    year.append(temp_list[i][9])

df2 = pd.DataFrame(list(zip(star_name,distance,mass,radius,year,consti)),columns=['Star_name','Distance','Mass','Radius','Discovery Year','Constellation'])

df2.to_csv('Scraper.csv')



