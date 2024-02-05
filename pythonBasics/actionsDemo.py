import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#Chrome driver - Chrome browser
# --Chrome
service_obj = Service() #seleniumManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(5) #global timeout, applies to all code
driver.maximize_window()

#5 seconds is max time out..
driver.get("https://rahulshettyacademy.com/AutomationPractice/#/")
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID, 'mousehover')).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, 'Top')).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Reload')).click().perform()