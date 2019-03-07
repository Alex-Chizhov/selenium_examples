from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
id = driver.find_element_by_xpath("//span[@id='glow-ingress-line2']").get_attribute('id')
print(id)

driver.quit()