from selenium import webdriver 
import time

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
driver.get('http://52.15.241.212:8082/')
driver.find_element_by_link_text("About Us").click()
text = driver.find_element_by_class_name("call-to-action").text
if text=="It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).":
    return 1
else:
    return 0
