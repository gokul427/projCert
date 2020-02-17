from selenium import webdriver 
import time

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get('http://52.15.241.212:8082/')
driver.find_element_by_link_text("About Us").click()
text = driver.find_element_by_class_name("call-to-action").text
print text
