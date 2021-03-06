from selenium import webdriver
import time

chrome_driver_path = "/Users/nakoya/Development/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element_by_css_selector("#cookie")


def click_cookie():
    timeout = 5
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        cookie.click()


def buy_upgrade():
    money = driver.find_element_by_css_selector("#money").text.replace(",", "")
    buy_cursor = driver.find_element_by_css_selector("#buyCursor")
    cursor_cost = driver.find_element_by_xpath('//*[@id="buyCursor"]/b').text.split()[-1].replace(",", "")
    buy_grandma = driver.find_element_by_css_selector("#buyGrandma")
    grandma_cost = driver.find_element_by_xpath('//*[@id="buyGrandma"]/b').text.split()[-1].replace(",", "")
    buy_factory = driver.find_element_by_css_selector("#buyFactory")
    factory_cost = driver.find_element_by_xpath('//*[@id="buyFactory"]/b').text.split()[-1].replace(",", "")
    buy_mine = driver.find_element_by_css_selector("#buyMine")
    mine_cost = driver.find_element_by_xpath('//*[@id="buyMine"]/b').text.split()[-1].replace(",", "")
    buy_shipment = driver.find_element_by_css_selector("#buyShipment")
    shipment_cost = driver.find_element_by_xpath('//*[@id="buyShipment"]/b').text.split()[-1].replace(",", "")
    buy_alchemy_lab = driver.find_element_by_css_selector("#buyAlchemy\ lab")
    alchemy_lab_cost = driver.find_element_by_xpath('//*[@id="buyAlchemy lab"]/b').text.split()[-1].replace(",", "")
    buy_portal = driver.find_element_by_css_selector("#buyPortal")
    portal_cost = driver.find_element_by_xpath('//*[@id="buyPortal"]/b').text.split()[-1].replace(",", "")
    buy_time_machine = driver.find_element_by_css_selector("#buyTime\ machine")
    time_machine_cost = driver.find_element_by_xpath('//*[@id="buyTime machine"]/b').text.split()[-1].replace(",", "")
    if int(money) >= int(time_machine_cost):
        buy_time_machine.click()
    elif int(money) >= int(portal_cost):
        buy_portal.click()
    elif int(money) >= int(alchemy_lab_cost):
        buy_alchemy_lab.click()
    elif int(money) >= int(shipment_cost):
        buy_shipment.click()
    elif int(money) >= int(mine_cost):
        buy_mine.click()
    elif int(money) >= int(factory_cost):
        buy_factory.click()
    elif int(money) >= int(grandma_cost):
        buy_grandma.click()
    elif int(money) >= int(cursor_cost):
        buy_cursor.click()


end_game = 300
start_game = time.time()
while time.time() < start_game + end_game:
    click_cookie()
    buy_upgrade()
results = driver.find_element_by_css_selector("#cps")
print(results.text)
driver.quit()
