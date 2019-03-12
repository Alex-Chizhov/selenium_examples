from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)
wait.until(EC.alert_is_present)
wait.until(EC.element_located_selection_state_to_be(locator, is_selected))
wait.until(EC.element_located_to_be_selected(locator))
wait.until(EC.element_selection_state_to_be(element, is_selected))
# and more in documentation
# https://seleniumhq.github.io/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.expected_conditions.html