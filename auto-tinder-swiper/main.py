import os
from selenium import webdriver, common
from time import sleep

CHROME_DRIVER_PATH = os.environ["CHROME_DRIVER_PATH"]
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get("https://tinder.com/")

sleep(5)
accept_cookies = driver.find_element_by_css_selector(
    "#s722988905 > div > div.Pos\(f\).Start\(0\).End\(0\).Z\(2\).Bxsh\(\$bxsh-4-way-spread\).B\(0\).Bgc\(\#fff\).C\(\$c-secondary\) > div > div > div:nth-child(1) > button")
accept_cookies.click()

sleep(5)
start_log_in = driver.find_element_by_css_selector(
    "#s722988905 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div > div > header > div > div:nth-child(2) > div.H\(40px\).Px\(28px\) > a")
start_log_in.click()

sleep(5)
log_in_with_google = driver.find_element_by_css_selector(
    "#s-1005392171 > div > div > div.Ta\(c\).H\(100\%\).D\(f\).Fxd\(c\).Pos\(r\) > div > div:nth-child(4) > span > div:nth-child(1) > div > button")
log_in_with_google.click()

driver.window_handles
base_window = driver.window_handles[0]
google_log_in_window = driver.window_handles[1]
driver.switch_to.window(google_log_in_window)

sleep(5)
email = driver.find_element_by_name("identifier")
email.send_keys(EMAIL)
sleep(1)
email_next_button = driver.find_element_by_css_selector("#identifierNext > div > button")
email_next_button.click()

sleep(5)
password = driver.find_element_by_name("password")
password.send_keys(PASSWORD)
sleep(1)
password_next_button = driver.find_element_by_css_selector("#passwordNext > div > button")
password_next_button.click()

sleep(2)
driver.switch_to.window(base_window)

sleep(5)
allow_location = driver.find_element_by_css_selector(
    "#s-1005392171 > div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Pos\(r\).Ov\(h\).C\(\#fff\).Bg\(\$c-pink\)\:h\:\:b.Bg\(\$c-pink\)\:f\:\:b.Bg\(\$c-pink\)\:a\:\:b.Trsdu\(\$fast\).Trsp\(\$background\).Bg\(\$primary-gradient\).button--primary-shadow.StyledButton.Fw\(\$semibold\).focus-button-style.W\(225px\).W\(a\)")
allow_location.click()

sleep(5)
no_notifications = driver.find_element_by_css_selector(
    "#s-1005392171 > div > div > div > div > div.Pb\(24px\).Px\(24px\).D\(f\).Fxd\(rr\).Ai\(st\) > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(40px\).Fw\(\$semibold\).focus-button-style.W\(a\).C\(\$c-bluegray\)")
no_notifications.click()

sleep(5)
swipe_left = driver.find_element_by_css_selector(
    "#s722988905 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.recsCardboard.W\(100\%\).Mt\(a\).H\(100\%\)--s.Px\(4px\)--s.Pos\(r\) > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Isolate.W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-pink\) > button")

for i in range(100):
    try:
        sleep(5)
        driver.execute_script('arguments[0].click()', swipe_left)
    except common.exceptions.NoSuchElementException:
        sleep(10)
    try:
        sleep(2)
        do_not_add_to_homepage = driver.find_element_by_css_selector(
            "#s-1005392171 > div > div > div.Pt\(12px\).Pb\(8px\).Px\(36px\).Px\(24px\)--s > button.button.Lts\(\$ls-s\).Z\(0\).CenterAlign.Mx\(a\).Cur\(p\).Tt\(u\).Ell.Bdrs\(100px\).Px\(24px\).Px\(20px\)--s.Py\(0\).Mih\(42px\)--s.Mih\(50px\)--ml.C\(\$c-secondary\).C\(\$c-base\)\:h.Fw\(\$semibold\).focus-button-style.D\(b\).Mx\(a\)")
        do_not_add_to_homepage.click()
    except common.exceptions.NoSuchElementException:
        pass

driver.quit()