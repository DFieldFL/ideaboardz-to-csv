import csv
import time

from bs4 import BeautifulSoup
from selenium import webdriver
import requests
from config import *

url = raw_input("Enter a ideaboardz url: ")
browser = webdriver.Firefox(executable_path = GECKO_DRIVER)
browser.get(url)
time.sleep(4)
soup = BeautifulSoup(browser.page_source, "html.parser")

with open('out.csv', 'wb') as csvfile:
    csvWriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

    columns = []
    for section in soup.find_all('div', class_='section'):
        sectionText = ''
        for sticky in section.find_all('div', class_='sticky'):
            stickyText = sticky.find('div', class_='stickyText').getText()
            stickyVotes = sticky.find('span', class_='count').getText()
            votes = ' (+' + stickyVotes + ')' if stickyVotes != '0' else ''
            sectionText += stickyText + votes + '\r\n'
        columns.append(sectionText)

    csvWriter.writerow(columns)

browser.quit()
