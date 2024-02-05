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
driver.get("https://rahulshettyacademy.com/loginpagePractise/#/")
driver.find_element(By.CSS_SELECTOR, '.blinkingText').click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])  # child window
print(driver.find_element(By.XPATH, '//div[@class="col-md-8"]/p[2]').text)
contextText = driver.find_element(By.XPATH, '//div[@class="col-md-8"]/p[2]').text
text = contextText.split()
print(text[4])
email = (text[4])
driver.close()

driver.switch_to.window(windowsOpened[0])  # parent window
print(driver.find_element(By.XPATH, '//div[@class="form-group"]/p/b[2]').text)
pwd = driver.find_element(By.XPATH, '//div[@class="form-group"]/p/b[2]').text

login = (driver.find_element(By.ID, 'username').send_keys(email))
password = (driver.find_element(By.ID, 'password').send_keys(pwd))

terms = driver.find_element(By.ID, 'terms')
if terms.is_selected():
    pass
else:
    terms.click()

#Click onto the button and fetch error message in alert
driver.find_element(By.ID, 'signInBtn').click()
wait = WebDriverWait(driver, 5)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

#TODO INSTRUCTOR VERSION
#import time

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# service_obj = Service("/Users/rahulshetty/documents/chromedriver")
# driver = webdriver.Chrome(service=service_obj)
# driver.implicitly_wait(4)
#
# driver.get("https://rahulshettyacademy.com/loginpagePractise/")
# driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
# windowsOpened = driver.window_handles
#
# driver.switch_to.window(windowsOpened[1])
# message = driver.find_element(By.CSS_SELECTOR, ".red").text
# var = message.split("at")[1].strip().split(" ")[0]
# driver.close()
# driver.switch_to.window(windowsOpened[0])
# driver.find_element(By.ID, "username").send_keys(var)
# driver.find_element(By.ID, "password").send_keys(var)
# driver.find_element(By.CSS_SELECTOR, "#signInBtn").click()
# wait = WebDriverWait(driver,10)
# wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
# print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)
