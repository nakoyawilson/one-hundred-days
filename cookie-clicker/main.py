from selenium import webdriver
import time

chrome_driver_path = "/Users/nakoya/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")
cookie = driver.find_element_by_css_selector("#bigCookie")

def click_cookie():
    timeout = 5
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        cookie.click()


def buy_item():
    store_items_objects = driver.find_elements_by_css_selector("#products .unlocked")
    store_items_objects[0].click()


end_game = 300
start_game = time.time()
while time.time() < start_game + end_game:
    click_cookie()
    buy_item()
cookies_per_second = driver.find_element_by_css_selector("#cookies").text.split("\n")[1]
print(cookies_per_second)
driver.quit()