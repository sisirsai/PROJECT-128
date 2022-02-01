from turtle import distance
from selenium import webdriver 
from bs4 import BeautifulSoup as bs
import time 
import csv
import pandas as pd
import requests

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = requests.get(start_url)
time.sleep(10)

soup = bs(browser.text , 'html.parser')
star_table = soup.find('table')
temp_list = []
table_rows = star_table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_name = []
distance = []
mass = []
lum = []
radius = []

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][1])
    lum.append(temp_list[i][7])
    distance.append(temp_list[i][3])
    radius.append(temp_list[i][6])
    mass.append(temp_list[i][5])

df2 = pd.DataFrame(list(zip(star_name,distance,mass,radius,lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])

df2.to_csv('Scraper1.csv')



