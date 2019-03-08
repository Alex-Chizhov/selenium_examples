from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)
element = driver.find_element_by_name("q")
