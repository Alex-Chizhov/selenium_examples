from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.find_element_by_xpath("//input[@id='search']").send_keys("selenium wd" + Keys.ENTER)

# if in field there is a mask-(text placeholder) you can use Keys.HOME
# or if there is a some text you can use this:
search_field = driver.find_element_by_xpath("//input[@id='search']")
search_field.send_keys(Keys.CONTROL + 'a' + Keys.NULL,
                       'python' + Keys.ENTER)

# Attach file
driver.get("https://radikalno.ru/")
driver.find_element_by_xpath("//input[@id='file']").send_keys('F:\\photo.jpg')
driver.find_element_by_xpath("//input[@id='upload_butt']").click()

driver.quit()