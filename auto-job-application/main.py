from selenium import webdriver
from time import sleep
import os

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_WRA=true&geoId=92000000&keywords=junior%20python%20developer&location=Worldwide"
LINKEDIN_EMAIL = os.environ["LINKEDIN_EMAIL"]
LINKEDIN_PASSWORD = os.environ["LINKEDIN_PASSWORD"]

chrome_driver_path = "/Users/nakoya/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(LINKEDIN_URL)

sleep(2)
sign_in = driver.find_element_by_css_selector("body > div.base-serp-page > header > nav > div > a.nav__button-secondary")
sign_in.click()

sleep(2)
email = driver.find_element_by_name("session_key")
email.send_keys(LINKEDIN_EMAIL)
password = driver.find_element_by_name("session_password")
password.send_keys(LINKEDIN_PASSWORD)
submit = driver.find_element_by_css_selector("#organic-div > form > div.login__form_action_container > button")
submit.click()

# sleep(2)
# job_listing = driver.find_element_by_css_selector(".job-card-container__link job-card-list__title")
# job_listing.click()
#
sleep(2)
easy_apply = driver.find_element_by_css_selector(".jobs-apply-button")
easy_apply.click()

sleep(2)
next_button = driver.find_element_by_css_selector(".justify-flex-end .artdeco-button--primary")
next_button.click()
sleep(2)
next_button.click()