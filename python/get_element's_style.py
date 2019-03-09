from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.ebay.com/')
color = driver.find_element_by_xpath('//input[@value="Search"]').value_of_css_property("color")
background = driver.find_element_by_xpath('//input[@value="Search"]').value_of_css_property("background")

print(color)
print(background)
driver.quit()