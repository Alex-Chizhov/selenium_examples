#  https://seleniumhq.github.io/selenium/docs/api/py/webdriver/selenium.webdriver.common.action_chains.html
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://materializecss.com/range.html")
spans = driver.find_elements_by_xpath("//div[@id='range-input']//span")
span1 = spans[0]
span2 = spans[1]

action = ActionChains(driver)
action.move_to_element(span1).click_and_hold()
action.move_to_element(span2).release()
action.perform()

time.sleep(10)
driver.quit()