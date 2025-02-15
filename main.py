import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import datetime
import json # json.loads converts the string dictionary to dictionary

options = ["popular", "newest"]
url = "https://www.rottentomatoes.com/browse/movies_in_theaters/sort:popular"
response = requests.get(url)
print(response)

soup = bs(response.text, "html.parser")
print(type(soup))
table = soup.find('script', type = "application/ld+json")
# for row in table:
#     print(row.text)
print(json.loads(table.text)["itemListElement"]["itemListElement"])
# print(soup.find_all('title').text)
# print(soup.find_all('meta'))