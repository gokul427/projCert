from selenium import webdriver 
import time

driver = webdriver.Firefox(executable_path='/Users/ghraj/Downloads/geckodriver')
driver.get('https://python.org')
driver.find_element_by_link_text("About").click()
text = driver.find_element_by_class_name("call-to-action").text
print text
