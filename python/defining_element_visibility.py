from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/howto/howto_css_contact_form.asp")
button = driver.find_element_by_xpath("//button")

if button.is_displayed():
    button.click()
