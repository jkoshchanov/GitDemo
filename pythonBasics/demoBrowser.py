from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.edge.service import Service

#Chrome driver - Chrome browser
# --Chrome
service_obj = Service() #seleniumManager
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service_obj)

# --Firefox
# service_obj = Service() #seleniumManager
# driver = webdriver.Firefox(service=service_obj)

# --Microsoft Edge
# service_obj = Service() #seleniumManager
# driver = webdriver.Edge(service=service_obj)


driver.get("https://www.rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
driver.close()


