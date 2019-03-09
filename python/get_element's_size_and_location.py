from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.w3.org/")

location = driver.find_element_by_xpath("//div[@id='search-form']").location
size = driver.find_element_by_xpath("//div[@id='search-form']").size

print(location)
print(size)

driver.quit()