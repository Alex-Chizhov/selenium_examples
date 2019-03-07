from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

my_cookies = [
    {'domain': '.youtube.com', 'expiry': 1551976989.859501, 'httpOnly': False, 'name': 'GPS', 'path': '/', 'secure': False, 'value': '1'},
    {'domain': '.youtube.com', 'httpOnly': True, 'name': 'YSC', 'path': '/', 'secure': False, 'value': 'DDMweYzkrWk'},
    {'domain': '.youtube.com', 'expiry': 1615047192, 'httpOnly': False, 'name': 'PREF', 'path': '/', 'secure': False, 'value': 'f1=50000000&f6=400'},
    {'domain': '.youtube.com', 'expiry': 1567527189.859558, 'httpOnly': True, 'name': 'VISITOR_INFO1_LIVE', 'path': '/', 'secure': False, 'value': 'GwDm5ob_Als'},
    {'domain': '.youtube.com', 'expiry': 2145916800.859575, 'httpOnly': False, 'name': 'CONSENT', 'path': '/', 'secure': False, 'value': 'WP.277801'},
              ]
for cookie in my_cookies:
    driver.add_cookie(cookie)

driver.refresh()
time.sleep(3)
driver.quit()

