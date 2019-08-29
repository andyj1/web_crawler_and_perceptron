#!/usr/bin/env python
# -*- coding: utf-8 -*-
# August, 2019
# Google Web Search Crawler

import argparse

import requests
from bs4 import BeautifulSoup

GOOGLE_URL = 'https://google.com/search?q=%s'

def search(search_keyword):
    # if search_keyword is empty, error
    if not search_keyword:
        raise ValueError
    
    # need to tailor to your device configurations/needs
    custom_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Whale/1.6.81.13 Safari/537.36'
    }
    
    # send a HTTP request through Google search qeury api
    result = requests.get(GOOGLE_URL % (search_keyword), headers = custom_headers)
    if result.status_code == 200:
        print("Success HTTP request. \n\n")
    # set 'lxml' as default parser for BeautifulSoup
    soup = BeautifulSoup(result.content, "lxml")
    searches = soup.find_all('div',attrs={'class':'g'})
    
    # retrieve url links from <link> tag - href
    urls = [];
    for div in searches:
        urls.append(div.find('a')['href'])
    
    # compile as a dictionary to display in JSON format
    result = []
    for res, url in zip(searches,urls): 
        temp = {}
        temp['link'] = url
        temp['title'] = res.text[0:20]
        result.append(temp)

    return result

if __name__ == '__main__':
    # query = 'test'
    parser = argparse.ArgumentParser()
    parser.add_argument('-q','--query', help="Enter a query word(sentence) to search... \n")
    args = parser.parse_args()
    query = args.query

    result = search(query)
    print(result)