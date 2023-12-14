from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

PROMISED_DOWN = 900
PROMISED_UP = 900
EMAIL = 'wxxxxxxxxx@gmail.com'
PASSWORD = 'whxxxxxxxx'
USERNAME = 'Grixxxxxxxx'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

        self.action = ActionChains(self.driver)

        self.down = PROMISED_DOWN
        self.up = PROMISED_UP

    def get_internet_speed(self):
        global download_speed, upload_speed
        self.driver.get("https://fast.com/#")
        time.sleep(15)
        self.speed = self.driver.find_element(
            By.XPATH, '//*[@id="speed-value"]')
        download_speed = self.speed.text
        print(download_speed)
        more_info = self.driver.find_element(By.ID, 'show-more-details-link')
        print(more_info.text)
        self.action.click(more_info)
        self.action.perform()
        time.sleep(30)
        self.upload = self.driver.find_element(
            By.XPATH, '//*[@id="upload-value"]')
        upload_speed = self.upload.text
        print(upload_speed)

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/?lang=en")
        time.sleep(5)
        log_in = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div')
        self.action.click(log_in)
        self.action.perform()
        time.sleep(5)
        click_email = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div')
        self.action.click(click_email)
        self.action.perform()
        enter_email = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        self.action.send_keys_to_element(enter_email, USERNAME)
        self.action.perform()
        next_button = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
        self.action.click(next_button)
        self.action.perform()
        time.sleep(5)
        enter_password = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        self.action.send_keys_to_element(enter_password, PASSWORD)
        self.action.perform()
        click_log_in = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        self.action.click(click_log_in)
        self.action.perform()
        time.sleep(10)
        tweet = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]')
        self.action.click(tweet)
        self.action.perform()
        time.sleep(10)
        tweet_text = self.driver.find_element(
            By.XPATH, "//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']")
        self.action.send_keys_to_element(tweet_text, f'Internet speed test results are Downlaod: {download_speed}, Upload: {upload_speed}')
        self.action.perform()
        post_tweet = self.driver.find_element(
            By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div')
        self.action.click(post_tweet)
        self.action.perform()
        self.driver.quit()


speed_check = InternetSpeedTwitterBot()
speed_check.get_internet_speed()

if int(download_speed) < PROMISED_DOWN and int(upload_speed) < PROMISED_UP:
    speed_check.tweet_at_provider()
