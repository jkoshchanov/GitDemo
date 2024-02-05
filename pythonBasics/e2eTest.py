from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Chrome driver - Chrome browser
# --Chrome
service_obj = Service() #seleniumManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(4)
driver.get("https://rahulshettyacademy.com/angularpractice")

#XPATH with partial expression
# //a[contains(@href,'shop')]
driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, 'div/h4/a').text
    if productName == "Blackberry":
        product.find_element(By.XPATH, 'div/button').click()

driver.find_element(By.XPATH, '//*[@id="navbarResponsive"]/ul/li/a').click()
driver.find_element(By.XPATH, '//button[@class="btn btn-success"]').click()
driver.find_element(By.ID, 'country').send_keys('Ind')
wait = WebDriverWait(driver,15)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT, 'India').click()
driver.find_element(By.XPATH, '//div[@class="checkbox checkbox-primary"]').click()
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
successText = driver.find_element(By.CLASS_NAME, "alert-success").text
assert "Success! Thank you!" in successText #using 'in' would partially check the test in the string for assertion
driver.close()


#CSS Selector with partial expression
# a[href* = 'shop')
# driver.find_element(By.CSS_SELECTOR, " a[href* ='shop']").click()

