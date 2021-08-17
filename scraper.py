from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(START_URL)

soup = BeautifulSoup(page.text, "html.parser")
headers = ["name", "distance", "mass", "radius","luminosity"]

def scrape():

    star_table = soup.find('table')
    temp_list= []
    table_rows = star_table.find_all('tr')
    for tr in table_rows:
        td_tags = tr.find_all('td')
        row = [i.text.rstrip() for i in td_tags]
        temp_list.append(row)
        # for index, td_tag in enumerate(td_tags):
        #         if (index==0):
        #             temp_list.append(td_tag.find_all("td")[0].contents[0])
        #         else:
        #             try:
        #                 temp_list.append(td_tag.contents[0])
        #             except: temp_list.append("")
        # stars_data.append(temp_list)
    star_name=[]
    distance=[]
    mass=[]
    radius=[]
    lum=[]

    for i in range(1, len(temp_list)):
        star_name.append(temp_list[i][1])
        distance.append(temp_list[i][3])
        mass.append(temp_list[i][5])
        radius.append(temp_list[i][6])
        lum.append(temp_list[i][7])

    df = pd.DataFrame(list(zip(star_name,distance,mass,radius,lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity']) 
    print(df) 
    df.to_csv('bright_stars.csv')

    # with open("scraper.csv", "w") as f:
    #     csv_writer = csv.writer(f)
    #     csv_writer.writerow(headers)
    #     csv_writer.writerows(stars_data)

scrape()