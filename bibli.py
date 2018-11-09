from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import os

from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()

driver = webdriver.Chrome()
driver.get("http://sagu.ent.sirsidynix.net/client/fr_FR/formation")

elem = driver.find_element_by_css_selector('.menuLink > a[tabindex="2"]')
elem.click()

loginiframe = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_css_selector('#loginModal > iframe'))

driver.switch_to.frame(loginiframe)

username = driver.find_element_by_id('j_username')
username.clear()
username.send_keys(os.getenv('CARD_NUMBER'))
password = driver.find_element_by_id('j_password')
password.send_keys(os.getenv('PASSWORD'))
password.send_keys(Keys.RETURN)


WebDriverWait(driver, 20).until(lambda driver: driver.find_element_by_id('checkoutsSummary'))
print('page loaded!!')

#does not work??
books = driver.find_elements_by_css_selector('.checkoutsBookInfo')
resultTitles = [r.text for r in books]
print('\n'.join(resultTitles))

driver.close()
