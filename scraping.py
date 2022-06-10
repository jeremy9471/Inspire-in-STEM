# !/usr/bin/python

################################################
#       web scraping
#       Name : Jeremy
#       Date: 7 / 6 / 22
#  #############################################
import requests
from bs4 import BeautifulSoup as bs

user_name = "jeremy9471" # Input username
url = "https://github.com/" + user_name # enter site URL
results = requests.get(url)

soup = bs(results.content,"html.parser")
profile_pic = soup.find('img',{'alt': 'Avatar'})['src']
print(profile_pic)