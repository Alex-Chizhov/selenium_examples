from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_extension('adblockpluschrome-3.4.2.2213.crx')
driver = webdriver.Chrome(options=options)
