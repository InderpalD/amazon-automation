from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


import re
import time

class amazon(object):

	#extract items from google sheet
	def __init__(self, items):
		self.url = 'https://www.amazon.com/'
		self.items = items
		self.profile = webdriver.FirefoxProfile()
		self.options = Options()
		self.driver = webdriver.Firefox(firefox_profile=self.profile,
										firefox_options=self.options)

		self.driver.get(self.url)


	#search amazon for items
	def search_items(self):
		urls=[]
		prices=[]
		names=[]

		for item in self.items:
			print(f'Seraching for {item}.')
			self.driver.get(self.url)
			search_input = self.driver.find_element_by_id("twotabsearchtextbox")
			search_input.send_keys(item)

			time.sleep(3)

			search_button = self.driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
			search_button.click()

			time.sleep(3)


items = ['toothpaste']
amazon = amazon(items)
amazon.search_items()
			

			


		
		
		
		


