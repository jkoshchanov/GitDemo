from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.edge.service import Service

name = 'JASUR KOSHCHANOV'
#Chrome driver - Chrome browser
# --Chrome
service_obj = Service() #seleniumManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR, '#name').send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alertObj = driver.switch_to.alert
alertText = alertObj.text
print(alertText)
assert name in alertText
alertObj.accept()
