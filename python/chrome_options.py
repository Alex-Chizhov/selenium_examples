from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--show-fps-counter")
wd = webdriver.Chrome(options=chrome_options)


# list of options:
# https://peter.sh/experiments/chromium-command-line-switches/