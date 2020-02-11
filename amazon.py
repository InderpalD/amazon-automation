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

			first_result = self.driver.find_element_by_id("result_0")
			asin = first_result.get_attribute("data-asin")
			product_url = "https://www.amazon.com/dp/" + asin
			price = self.get_product_price(product_url)
			name = self.get_product_name(product_url)

			prices.append(price)
			names.append(name)
			urls.append(product_url)

			print(name, price, product_url)

			time.sleep(3)

		return prices, urls, names

	def get_product_price(self, url):
		self.driver.get(url)
		try:
			price = self.driver.find_element_by_id("priceblock_ourprice")
		except:
			pass

		try:
			price = self.driver.find_element_by_id("priceblock_dealprice")
		except:
			pass
		

		if price is None:
			price = "Not Available"

		else:
			non_decimal = re.compile(r'[^\d.]+')
			price = non_decimal.sub('', price)

		return price


	def get_product_name(self, url):
		self.driver.get(url)
		try:
			product_name = self.driver.find_element_by_id("productTitle")
		except:
			pass

		if product_name is None:
			product_name = "Not available"

		return product_name


items = ['toothpaste']
amazon = amazon(items)
amazon.search_items()
			

			


		
		
