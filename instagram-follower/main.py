import os
from selenium import webdriver, common
from time import sleep

CHROME_DRIVER_PATH = "/Users/nakoya/Development/chromedriver"
SIMILAR_ACCOUNT = "pycoders"
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


class InstaFollower:

    def __init__(self, browser_driver_path):
        self.driver = webdriver.Chrome(executable_path=browser_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(1)
        username = self.driver.find_element_by_name("username")
        username.send_keys(USERNAME)
        sleep(1)
        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)
        sleep(1)
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()
        sleep(2)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/" + SIMILAR_ACCOUNT)
        sleep(2)
        followers_list = self.driver.find_element_by_partial_link_text("followers")
        followers_list.click()
        sleep(2)
        follower_popup = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        for i in range(20):
            sleep(5)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_popup)

    def follow(self):
        follow_buttons = self.driver.find_elements_by_css_selector("button.sqdOP.L3NKy.y3zKF")
        all_follow_buttons = [button for button in follow_buttons]
        for follow_button in all_follow_buttons:
            sleep(4)
            follow_button.click()
        sleep(1)
        self.driver.quit()


insta_follower_bot = InstaFollower(CHROME_DRIVER_PATH)
insta_follower_bot.login()
insta_follower_bot.find_followers()
insta_follower_bot.follow()