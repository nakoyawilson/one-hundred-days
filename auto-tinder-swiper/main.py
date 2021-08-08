import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

CHROME_DRIVER_PATH = os.environ["CHROME_DRIVER_PATH"]
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("https://tinder.com/")

sleep(2)
accept_cookies = driver.find_element_by_css_selector("#s722988905 > div > div.Pos\(f\).Start\(0\).End\(0\).Z\(2\).Bxsh\(\$bxsh-4-way-spread\).B\(0\).Bgc\(\#fff\).C\(\$c-secondary\) > div > div > div:nth-child(1) > button")
accept_cookies.click()

sleep(2)
start_log_in = driver.find_element_by_css_selector("#s722988905 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > header > div > div:nth-child(2) > div.H\(40px\).Px\(28px\) > a")
start_log_in.click()

sleep(3)
log_in_with_google = driver.find_element_by_css_selector("#s-1005392171 > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div:nth-child(4) > span > div:nth-child(1) > div > button")
log_in_with_google.click()