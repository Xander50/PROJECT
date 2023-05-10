from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests
# NASA Exoplanet URL
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page=requests.get(START_URL)
# Webdriver
soup=bs(page.text,'html.parser')

star_table=soup.find('table')
#total_table=len(star_table)

temp_list=[]
table_rows=star_table.find_all('tr')

for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names=[]
Distance=[]
Mass=[]
Radius=[]
Lum=[]


print(temp_list)

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Lum.append(temp_list[i][7])
    Radius.append(temp_list[i][6])

# Define Header
headers = ["Star_name","Distance","Mass","Radius","Luminosity"]

# Define pandas DataFrame   
df2=pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_names','Distance','Mass','Radius','Luminosity'])

# Convert to CSV
df2.to_csv("bright__stars.csv",index=True,index_label="id")
    


