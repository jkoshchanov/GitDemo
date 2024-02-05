import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.edge.service import Service

#Chrome driver - Chrome browser
# --Chrome
service_obj = Service() #seleniumManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(5) #global timeout

#5 seconds is max time out..
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, '.search-keyword').send_keys('ber')
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")#list[]
count = len(results)
assert count == 3
for result in results:
    result.find_element(By.XPATH,"div/button").click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

print(driver.find_element(By.CLASS_NAME, 'promoInfo').text)