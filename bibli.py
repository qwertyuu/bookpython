from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://sagu.ent.sirsidynix.net/client/fr_FR/formation")

elem = driver.find_element_by_css_selector('.menuLink > a[tabindex="2"]')
elem.click()

driver.close()
