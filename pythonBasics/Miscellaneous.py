from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless") #headless mode means that browser would NOT open but scripts still execute as expected
chrome_options.add_argument("--ignore-certificate-errors") #this would ignore and continue executing scripts when page requires certificated access

# Chrome driver - Chrome browser
# --Chrome
service_obj = Service()  # seleniumManager
driver = webdriver.Chrome(options=chrome_options, service=service_obj)
driver.implicitly_wait(5)  # global timeout, applies to all code

# 5 seconds is max time out..
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#using python in selenium with JavaScript actions
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
driver.get_screenshot_as_file("screen.png")