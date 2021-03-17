# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 16:47:11 2021

@author: Nouman Ahmad
"""

import bs4
from  bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url = "https://news.google.com/news/rss" 

root=urlopen(news_url)

xml_page = root.read()

root.close()

soup_page = soup(xml_page,"xml")

news_list = soup_page.findAll("item")
 
for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print("_"*30)
    