from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://pagination.js.org/")
li_1 = driver.find_element_by_xpath("//div[@id='demo1']//div[@class='data-container']//li[1]")
print(li_1.text)
next_button = driver.find_element_by_xpath("//div[@class='paginationjs']//a[contains(text(),'»')]").click()

# Waiting of disappear old element. Implicit expectations do Not affect!
wait = WebDriverWait(driver, 10)
wait.until(EC.staleness_of(li_1))

li_11 = driver.find_element_by_xpath("//div[@id='demo1']//div[@class='data-container']//li[1]")
print(li_11.text)
driver.quit()