from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

results = driver.find_elements_by_css_selector('.list-recent-events > li > h3:nth-child(1) > a:nth-child(1)')
resultTitles = [r.text for r in results]
print('\n'.join(resultTitles))

driver.close()
