from selenium import webdriver
from selenium.webdriver import ChromeOptions


options = ChromeOptions()
desired_caps = options.to_capabilities()
desired_caps['platform'] = 'Linux'
browser = webdriver.Remote(
        desired_capabilities=desired_caps
    )