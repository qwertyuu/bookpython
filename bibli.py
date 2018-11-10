from pprint import pprint

from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.common.keys import Keys
import os

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from book import Book

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
print('Logged in!!')

locator = driver.find_element_by_css_selector('.myAccountLoadingHolder')
WebDriverWait(driver, 10).until(expected_conditions.invisibility_of_element_located(locator))
print('books fetched')
dom_books = driver.find_elements_by_css_selector('.checkoutsLine')

book_objects = []
for dom_book in dom_books:
    book_object = Book()
    book_object.author = dom_book.find_element_by_class_name('checkouts_author').text
    book_object.due_date = dom_book.find_element_by_class_name('checkoutsDueDate').text
    book_object.renewed = int(dom_book.find_element_by_class_name('checkoutsRenewCount').text)
    book_object.id = dom_book.find_element_by_class_name('checkouts_itemId').text
    book_object.title = dom_book.find_element_by_class_name('hideIE').text
    book_object.print()
    book_objects.append(book_object)


driver.close()
