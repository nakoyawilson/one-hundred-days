import os
from selenium import webdriver

PROMISED_DOWN = 100
PROMISED_UP = 100
CHROME_DRIVER_PATH = "/Users/nakoya/Development/chromedriver"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]


class InternetSpeedTwitterBot:

    def __init__(self, browser_driver_path):
        self.driver = webdriver.Chrome(executable_path=browser_driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


internet_speed_twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
internet_speed_twitter_bot.get_internet_speed()
internet_speed_twitter_bot.tweet_at_provider()
