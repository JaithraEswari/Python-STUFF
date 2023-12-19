from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
import requests

RENT_URL = 'https://appbrewery.github.io/Zillow-Clone/'
GOOGLE_FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSfLXE3r8tehaxUmo0aqS7RQqMq7CCaB-DcYzzRHSDvYvWxdKQ/viewform?usp=sf_link'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding':'gzip, deflate, br'
}

response = requests.get(url=RENT_URL, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

property_link = soup.select('ul.List-c11n-8-84-3-photo-cards li div div article div div.StyledPropertyCardDataWrapper a')
links = [link['href'] for link in property_link]

property_price = soup.select('ul.List-c11n-8-84-3-photo-cards li div div article div div div div.PropertyCardWrapper span')
prices = [price.text.strip('+ 1 /mobd') for price in property_price]

property_address = soup.select('ul.List-c11n-8-84-3-photo-cards li div div article div div.StyledPropertyCardDataWrapper a address')
address = [address.text.strip().replace('|', '') for address in property_address]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
action = ActionChains(driver)



for i in range(0, len(property_address)):
    driver.get(GOOGLE_FORM)
    time.sleep(2)

    option1 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    action.click(option1)
    action.perform()
    action.send_keys(address[i])
    action.perform()
    time.sleep(2)

    option2 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    action.click(option2)
    action.perform()
    action.send_keys(prices[i])
    action.perform()
    time.sleep(2)

    option3 = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    action.click(option3)
    action.perform()
    action.send_keys(links[i]) # type: ignore
    action.perform()
    time.sleep(2)

    click = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    action.click(click)
    action.perform()
    time.sleep(2)

driver.quit()