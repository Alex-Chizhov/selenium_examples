from selenium import webdriver
import time

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": "C:\\MyNewFolder",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
         }
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)


driver.get("https://docs.google.com/presentation/d/1n2TEPRiaRajUODFNNbNQCfKIwnSViLia8G9PWSlMAow/export/pptx")
time.sleep(1)
driver.quit()
