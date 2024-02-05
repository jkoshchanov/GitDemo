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

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

print(len(checkboxes))

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break

radioButtons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radioButtons[1].click()
assert radioButtons[1].is_selected()

assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, 'hide-textbox').click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()