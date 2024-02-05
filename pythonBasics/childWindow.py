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

#5 seconds is max time out..
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT, "Click Here").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1]) #child window
print(driver.find_element(By.TAG_NAME, 'h3').text)
driver.close()

driver.switch_to.window(windowsOpened[0]) #parent window
assert "Opening a new window" == driver.find_element(By.TAG_NAME, 'h3').text