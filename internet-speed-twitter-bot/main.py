import os
from selenium import webdriver
from time import sleep

PROMISED_DOWN = 100
PROMISED_UP = 100
CHROME_DRIVER_PATH = "/Users/nakoya/Development/chromedriver"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


class InternetSpeedTwitterBot:

    def __init__(self, browser_driver_path):
        self.driver = webdriver.Chrome(executable_path=browser_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_test = self.driver.find_element_by_css_selector(".start-button")
        sleep(2)
        start_test.click()
        sleep(60)
        download_speed = self.driver.find_element_by_css_selector(".download-speed")
        upload_speed = self.driver.find_element_by_css_selector(".upload-speed")
        self.down = float(download_speed.text)
        self.up = float(upload_speed.text)
        sleep(2)
        self.driver.quit()

    def tweet_at_provider(self):
        pass

internet_speed_twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
internet_speed_twitter_bot.get_internet_speed()
internet_speed_twitter_bot.tweet_at_provider()
