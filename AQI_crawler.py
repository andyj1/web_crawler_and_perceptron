#!/usr/bin/env python
# -*- coding: utf-8 -*-
# August, 2019
# Korea Air Quality Index Web Crawler


import argparse
from googletrans import Translator
from urllib.request import urlopen
from bs4 import BeautifulSoup

def _translate(translator, word):
    translated_word = translator.translate(word, dest='en')
    return translated_word.text

def get_data(url):
    data = {}
    
    http = urlopen(targetUrl)
    html = http.read()
    soupData = BeautifulSoup(html, 'lxml')
    # information: location, time, index
    loc = soupData.find('a', id='aqiwgttitle1')
    time = soupData.find('span', id='aqiwgtutime')
    aqi = soupData.find('div', id='aqiwgtvalue')
        
    data['loc'] = loc.string
    data['time'] = time.string
    data['status'] = aqi.get('title')
    data['aqi'] = aqi.string
    
    return data

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--city', help="Enter name of city to get AQI (Air quality index)... \n", default="seoul")
    parser.add_argument('-n','--country', help="Enter name of country of the city \n", default="kr")
    args = parser.parse_args()
    city = args.city
    country = args.country
    
    # accepted: seoul/kr, usa/newyork

    # http://aqicn.org/city/seoul/kr/
    # http://aqicn.org/city/usa/newyork/
    targetUrl = 'http://aqicn.org/city/%s/%s' % (city, country)
    print('Reading... ',targetUrl)
    data = get_data(targetUrl)
    
    translator = Translator()
    location = str(_translate(translator, data['loc'].split()[0]))+' '+str(_translate(translator, data['loc'].split()[1]))
    time_day = _translate(translator, data['time'].split()[0])
    time_hour = _translate(translator, data['time'].split()[1][0:2])
    time = str(time_day)+' '+str(time_hour)
    status = _translate(translator, data['status'])
    index = _translate(translator, data['aqi'])
    
    # adjustment for translation
    if status.lower() == 'usually':
        status = 'Moderate'
    
    print('Air Quality Index for %s at %s is %s [Index: %s]' %  (location, time, status, index))