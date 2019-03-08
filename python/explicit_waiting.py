from selenium import webdriver
# setting explicit  waiting
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10) # seconds
# note that the locator is transmitted as a tuple
element = wait.until(EC.presence_of_element_located((By.NAME, "q")))
