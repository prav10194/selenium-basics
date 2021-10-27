# enable ssl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys 
from time import sleep

# opening a firefox in headless mode
options = Options()
options.headless = True

# passing the geckodriver in the executable path
driver = webdriver.Firefox(options=options, executable_path='./geckodriver')

driver.get("https://www.wikihow.com/Main-Page")

# wait for 'hp_coauthor' element to be visible on the page
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'hp_coauthor')))
    sleep(10)
except TimeoutException:
    print('Page timed out after 10 secs.')

soup = BeautifulSoup(driver.page_source, 'html.parser')

# find_all div with id = 'hp_coauthor'
expert_co_authored_articles_div = soup.find_all("div", {"id": "hp_coauthor"})[0]

# find_all div with class = 'hp_thumb'
expert_co_authored_articles = expert_co_authored_articles_div.find_all("div", {"class": "hp_thumb"})

# for each article retrieve the 'p' and 'a' tags 
for article in expert_co_authored_articles:
    str = "Title: " + article.find_all("p")[0].get_text() + "\n" + "Link: " + "https://www.wikihow.com/" + article.find_all("a")[0].get('href') + "\n\n"
    print(str) 
