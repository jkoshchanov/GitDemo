from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.edge.service import Service

#Chrome driver - Chrome browser
# --Chrome
service_obj = Service() #seleniumManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")

# ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.NAME, "email").send_keys("selenium@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456")
driver.find_element(By.ID, "exampleCheck1").click()

# Xpath - //tagname[@attribute='value'] -> //input[@type='submit']
# CSS - tagname[@attribute='value'] -> //input[@type='submit'], #id, .classname [css is better and faster than xpath]
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Jasur")
# driver.find_element(By.CSS_SELECTOR, "inlineRadio1").click()

#Static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")



driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message


driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys(" hello again !")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
driver.close()