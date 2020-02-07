# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16NPlOScQBWZqAlJzBBpDBAepAZSbHku5
"""

'''
Savannah Adkins
February 7, 2020
Lab 3
Python 3, in colab
'''

import requests
from bs4 import BeautifulSoup


lat = '35.2828'
lon = '-120.6596'


url = 'https://forecast.weather.gov/MapClick.php?lat='+lat+"&lon="+lon


page = requests.get(url)


soup=BeautifulSoup(page.content,"html.parser")

cur_weather_conditions = soup.find(id="current_conditions-summary")

cur_weather_conditions = cur_weather_conditions.text


print('The Current Weather Conditions at '+ lat +  ", " + lon + " is:" + cur_weather_conditions)