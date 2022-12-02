#SELENIUM CHEATSHEET

#WORKFLOW

from selenium import webdriver
web='www.google.com'
path='introduce chromedriver path'
driver.get(web)

# find an element
driver.find_element_by_id('name')

# find elements
driver.find_elements_by_class_name()
driver.find_elements_by_css_selector
driver.find_elements_by_xpath()
driver.find_elements_by_tag_name()
driver.find_elements_by_name()

# quit driver
driver.quit()

#getting the text
data = element.text

#implicit waits
import time
time.sleep(2)

# explicit waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

WDW(driver,5).until(EC.element_to_be_clickable((By.ID,'id_name'))) #Wait 5 seconds until an element is clickable

