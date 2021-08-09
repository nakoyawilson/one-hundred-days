from selenium import webdriver
from time import sleep
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_AL=true&f_WRA=true&geoId=92000000&keywords=junior%20python%20developer&location=Worldwide"
LINKEDIN_EMAIL = os.environ["LINKEDIN_EMAIL"]
LINKEDIN_PASSWORD = os.environ["LINKEDIN_PASSWORD"]

chrome_driver_path = "/Users/nakoya/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(LINKEDIN_URL)

sleep(3)
sign_in = driver.find_element_by_css_selector(
    "body > div.base-serp-page > header > nav > div > a.nav__button-secondary")
sign_in.click()
sleep(2)
email = driver.find_element_by_name("session_key")
email.send_keys(LINKEDIN_EMAIL)
sleep(2)
password = driver.find_element_by_name("session_password")
password.send_keys(LINKEDIN_PASSWORD)
sleep(2)
submit = driver.find_element_by_css_selector("#organic-div > form > div.login__form_action_container > button")
submit.click()

sleep(5)
driver.fullscreen_window()

sleep(2)
search_results = driver.find_element_by_css_selector("body > div.application-outlet > div.authentication-outlet > div.job-search-ext > div > div > section.jobs-search__left-rail > div > div")
search_results.click()
job_listings = []
while len(job_listings) < 25:
    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.PAGE_DOWN)
    try:
        links = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".job-card-container a"))
        )
    finally:
        job_listings = [link for link in links if link.get_attribute("tabindex") == "0"]

sleep(2)
for job in job_listings:
    sleep(2)
    job.click()

    sleep(2)
    save_button = driver.find_element_by_css_selector(".jobs-save-button")
    save_button.click()

    sleep(2)
    dismiss_notification = driver.find_element_by_css_selector(".artdeco-toast-item__dismiss")
    dismiss_notification.click()

    sleep(2)
    job_content = driver.find_element_by_css_selector("body > div.application-outlet > div.authentication-outlet > div.job-search-ext > div > div > section.jobs-search__right-rail")
    job_content.click()
    html = driver.find_element_by_tag_name("html")
    html.send_keys(Keys.END)

    sleep(2)
    follow_button = driver.find_element_by_css_selector(".jobs-company button")
    follow_button.click()

    sleep(2)
    dismiss_notification = driver.find_element_by_css_selector(".artdeco-toast-item__dismiss")
    dismiss_notification.click()

driver.quit()

