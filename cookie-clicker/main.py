from selenium import webdriver, common
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
    store_items_text = [item_object.text.split("\n") for item_object in store_items_objects]
    money = int(driver.find_element_by_css_selector("#cookies").text.split("\n")[0].split()[0].replace(",", ""))
    for index, product in reversed(list(enumerate(store_items_objects))):
        if money > int(store_items_text[index][1].replace(",","")):
            driver.execute_script('arguments[0].click()', store_items_objects[index])
            break


def buy_upgrade():
    upgrades = driver.find_elements_by_css_selector("#upgrades .enabled")
    if len(upgrades) > 0:
        try:
            driver.execute_script('arguments[0].click()', driver.find_element_by_xpath('//*[@id="upgrade0"]'))
        except common.exceptions.StaleElementReferenceException:
            pass


end_game = 300
start_game = time.time()
while time.time() < start_game + end_game:
    click_cookie()
    buy_item()
    buy_upgrade()
cookies_per_second = driver.find_element_by_css_selector("#cookies").text.split("\n")[1]
print(cookies_per_second)
driver.quit()