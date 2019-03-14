"""
This code works to scrape all html from
an infinite scroll page.
Code from https://michaeljsanders.com/2017/05/12/scrapin-and-scrollin.html
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

driver = webdriver.Chrome('C:/Users/romyj/Documents/UF/Senior/webapps/python/scraping/chromedriver')
driver.get('https://www.fbi.gov/wanted/fugitives');


lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
                lastCount = lenOfPage
                time.sleep(3)
                lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
                if lastCount==lenOfPage:
                    match=True

html = driver.page_source
bsObj = BeautifulSoup(html, "html.parser")

f = open('fbi.txt', 'w')
fName = open('fbinames.txt', 'w')

#url_list = []

people = bsObj.find_all( "p", {"class":"name"} )
for person in people:
    link = person.find('a')
    if 'href' in link.attrs:
        f.write(link.attrs['href'] +  '\n')
        #fName.write(link.get_text() + '\n')
        #url_list.append(link.attrs['href'])

#print(url_list)

f.close()
fName.close()

#def fugitive_details(url_list):
    #html = urlopen(url_list)
    #bsObj = BeautifulSoup(html, "html.parser")
    #name = bsObj.find("h1", {"class": "documentFirstHeading"}).get_text()
    #time.sleep(1)
    #print(name)
    #return name

#for url in url_list:
    #import requests
    #session = requests.Session()
    #hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
               #'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               #'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               #'Accept-Encoding': 'none',
               #'Accept-Language': 'en-US,en;q=0.8',
               #'Connection': 'keep-alive'}
    #url = url
    #req = session.get(url, headers=hdr)
    #fugitive_details(url)
