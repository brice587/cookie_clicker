from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

URL = "https://orteil.dashnet.org/cookieclicker/"


def cookie_clicker(cookie):
    cookie.click()


def number_of_cookies(drive):
    cookies = drive.find_element(By.XPATH, '//*[@id="cookies"]')
    cookie_number_text = cookies.text
    cookie_list = cookie_number_text.split(" ")
    cookie_number_str = cookie_list[0].replace(",", "")
    cookie_number = int(cookie_number_str)
    # print(cookie_number)
    return cookie_number


def upgrade():
    try:
        driver.find_element(By.CSS_SELECTOR, "#upgrades .enabled").click()
    except NoSuchElementException:
        return


def buy():
    upgrade()
    goods = driver.find_elements(By.CSS_SELECTOR, "#products .product.unlocked.enabled")
    for item in reversed(goods):
        item.click()


chrome_driver_path = "C:\\chromedriver.exe"
driver = webdriver.Chrome(service=Service(chrome_driver_path))

driver.get(URL)
time.sleep(3)

english = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
english.click()
time.sleep(3)

big_cookie = driver.find_element(By.ID, 'bigCookie')
time_check = time.time() + 1
time_end = time.time() + 60*5

while True:
    cookie_clicker(big_cookie)
    if time.time() >= time_check:
        # cookies_count = number_of_cookies(driver)

        buy()
        # print(buy_product)
        time_check = time.time() + 1

    if time.time() > time_end:
        rate = driver.find_element(By.ID, 'cookies')
        print(f'Cookies/Second: {rate.text.split()[-1]}')
        break
