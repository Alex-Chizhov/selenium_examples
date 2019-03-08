from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost/litecart/")

# properties from element you can see in chrome dev tools
name = driver.find_element_by_xpath("//button[@name='login']").get_attribute('name')
tagName = driver.find_element_by_xpath("//button[@name='login']").get_attribute('tagName')
textContent = driver.find_element_by_xpath("//button[@name='login']").get_attribute('textContent')
clientWidth = driver.find_element_by_xpath("//button[@name='login']").get_attribute('clientWidth')
outerHTML = driver.find_element_by_xpath("//button[@name='login']").get_attribute('outerHTML')

print(name, tagName, textContent, clientWidth)
print(outerHTML)
driver.quit()

# to get text from input or textarea use .get_attribute('value')
input = driver.find_element_by_xpath("//button[@name='login']").get_attribute('value')
