from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Chrome driver - Chrome browser
# --Chrome
service_obj = Service()  # seleniumManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(3)  # global timeout, applies to all code

# 5 seconds is max time out..
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.ID, 'tinymce').clear()
driver.find_element(By.ID, 'tinymce').send_keys('i am able to automate frames')
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR, 'h3').text)