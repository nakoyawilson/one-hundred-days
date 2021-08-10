import os
from selenium import webdriver
from time import sleep

PROMISED_DOWN = 100
PROMISED_UP = 100
CHROME_DRIVER_PATH = "/Users/nakoya/Development/chromedriver"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
INTERNET_PROVIDER = "@DigicelTT"


class InternetSpeedTwitterBot:

    def __init__(self, browser_driver_path):
        self.driver = webdriver.Chrome(executable_path=browser_driver_path)
        self.down = ""
        self.up = ""

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        start_test = self.driver.find_element_by_css_selector(".start-button")
        sleep(2)
        start_test.click()
        sleep(60)
        download_speed = self.driver.find_element_by_css_selector(".download-speed")
        upload_speed = self.driver.find_element_by_css_selector(".upload-speed")
        self.down = download_speed.text
        self.up = upload_speed.text

    def tweet_at_provider(self):
        if float(self.down) < PROMISED_DOWN * 0.9 or float(self.up) < PROMISED_UP * 0.9:
            self.driver.get("https://twitter.com/login")
            sleep(2)
            username = self.driver.find_element_by_name("session[username_or_email]")
            username.send_keys(TWITTER_EMAIL)
            password = self.driver.find_element_by_name("session[password]")
            password.send_keys(TWITTER_PASSWORD)
            login_button = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div')
            login_button.click()
            sleep(2)
            message = f"Hey {INTERNET_PROVIDER}, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            text_box = self.driver.find_element_by_css_selector(".public-DraftStyleDefault-block")
            text_box.send_keys(message)
            sleep(1)
            tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            tweet.click()
            sleep(5)
            self.driver.quit()


internet_speed_twitter_bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
internet_speed_twitter_bot.get_internet_speed()
internet_speed_twitter_bot.tweet_at_provider()

