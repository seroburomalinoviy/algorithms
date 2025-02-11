from datetime import date, datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as req

url = "https://tickets.lakhta.events/event/23FA307410B1F9BE84842D1ABE30D6AB48EA2CF8/2025-02-07"

browser = webdriver.Safari()
browser.get(url)

# soup = BeautifulSoup(req.urlopen(url).read(), 'html.parser')
soup = BeautifulSoup(browser.page_source, 'html.parser')

print(soup.get_text)

print(soup.find_all('div'))

# day = date.today()
# print(day)



