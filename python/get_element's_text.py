from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/html/html_forms.asp")

text = driver.find_element_by_xpath("//div[@class='w3-right w3-hide-small w3-wide toptext']").text
print(text)

# for inputs and textarea you must use
input_text = driver.find_element_by_xpath("//div[@class='w3-example']//input[@name='firstname']").get_attribute('value')
print(input_text)

driver.quit()
