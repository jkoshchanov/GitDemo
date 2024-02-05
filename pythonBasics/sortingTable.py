from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

browserSortedVeggies = []

# Chrome driver - Chrome browser
# --Chrome
service_obj = Service()  # seleniumManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(2)  # global timeout, applies to all code

# 5 seconds is max time out..
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")

# click on column header to sort
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()  # <span>Veg/fruit name</span> in inspected elements

# collect all veggie names -> BrowserSortedVeggieList (B,A,C)
veggieWevElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for element in veggieWevElements:
    browserSortedVeggies.append(element.text)

originalBrowserSortedList = browserSortedVeggies.copy()

# Sort this BrowserSortedVeggieList -> newSortedList (A,B,C)
browserSortedVeggies.sort()

# BrowserSortedVeggieList should be == newSortedList
assert browserSortedVeggies == originalBrowserSortedList
