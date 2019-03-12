from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("https://www.google.com/")

driver.execute_script("document.getElementById('hplogo').style.display = 'none';")
logo = driver.find_element_by_xpath("//div[@id='hplogo']")
print(logo.value_of_css_property('display'))    # none

driver.execute_script("document.getElementById('hplogo').style.display = 'block';")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of(logo))

logo = driver.find_element_by_xpath("//div[@id='hplogo']")
print(logo.value_of_css_property('display'))    # block

driver.quit()
