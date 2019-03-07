from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/howto/howto_css_contact_form.asp")
form = driver.find_element_by_xpath("//div[@class='test']")
form.find_element_by_xpath(".//input[@id='fname']").send_keys("Bob")
form.find_element_by_xpath(".//input[@id='lname']").send_keys("Simmons")
form.find_element_by_xpath(".//select[@id='country']").send_keys("Canada")
form.find_element_by_xpath(".//textarea").send_keys("Some text")

driver.quit()