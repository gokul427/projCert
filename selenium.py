from selenium import webdriver 
import time

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get('http://52.15.241.212:8082/')
driver.find_element_by_link_text("About Us").click()
text = driver.find_element_by_class_name("call-to-action").text
if text=="This is about page. Lorem Ipsum Dipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.":
    return 1
else:
    return 0
