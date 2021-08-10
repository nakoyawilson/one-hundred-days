import os
from selenium import webdriver
from time import sleep

CHROME_DRIVER_PATH = "/Users/nakoya/Development/chromedriver"
SIMILAR_ACCOUNT = "python.hub"
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


class InstaFollower:

    def __init__(self, browser_driver_path):
        self.driver = webdriver.Chrome(executable_path=browser_driver_path)

    def login(self):
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


insta_follower_bot = InstaFollower(CHROME_DRIVER_PATH)
insta_follower_bot.login()
insta_follower_bot.find_followers()
insta_follower_bot.follow()