from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
import time

USERNAME = 'whymegod2002'
PASSWORD = 'Whymegod2023'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True) 

class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.action = ActionChains(self.driver)
    
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)

        user_login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.action.click(user_login)
        self.action.perform()
        self.action.send_keys_to_element(user_login, USERNAME)
        self.action.perform()

        password_login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.action.click(password_login)
        self.action.perform()
        self.action.send_keys_to_element(password_login, PASSWORD)
        self.action.perform()

        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
        self.action.click(login_button)
        self.action.perform()
        time.sleep(5)

        save_login_button = self.driver.find_element(By.XPATH, '//div[contains(text(), "Not now")]')
        if save_login_button:
            self.action.click(save_login_button)
            self.action.perform()
            time.sleep(5)

        notification_button = self.driver.find_element(By.XPATH, '//button[contains(text(), "Not Now")]')
        if notification_button:
            self.action.click(notification_button)
            self.action.perform()
            time.sleep(5)

    def find_followers(self):
        self.driver.get('https://www.instagram.com/chefsteps/followers')
        time.sleep(10)

        scroll = self.driver.find_element(By.CLASS_NAME, '_aano')
        n = 0
        while n < 5:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', scroll)
            time.sleep(5)
            n += 1

    def follow(self):
        self.driver.get('https://www.instagram.com/chefsteps/followers')
        time.sleep(10)

        i = 1
        while i < 5:
            # cancel = self.driver.find_element(By.XPATH, '//button[contains(text(), "Cancel")]')
            # if cancel:
            #     self.action.click(cancel)
            #     self.action.perform()
            #     time.sleep(5)
            follow = self.driver.find_elements(By.XPATH, '//div[contains(text(), "Follow")]')
            self.action.click(follow[i])
            self.action.perform()
            time.sleep(2)
            i += 1



instagram = InstaFollower()
instagram.login()
# instagram.find_followers()
instagram.follow()