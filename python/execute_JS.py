from selenium import webdriver


driver = webdriver.Chrome()
links = driver.execute_script("return $$('a:contains((WebDriver)')")