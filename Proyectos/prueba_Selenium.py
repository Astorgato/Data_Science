from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://python.org/")
driver.implicitly_wait(30)
driver.close()