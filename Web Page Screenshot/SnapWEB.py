# Example of getting a web page snapshot using Selenium and Chrome Driver
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import random

# script_name = sys.argv[0]
options = Options()
options.add_argument('--headless')
# options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
try:
    driver.get(
        'https://www.google.com/')
    page_width = driver.execute_script('return document.body.scrollWidth')
    page_height = driver.execute_script('return document.body.scrollHeight')
    driver.set_window_size(page_width, page_height)

    driver.save_screenshot('Anything.png')
    driver.quit()
    print('Screenshot saved')
except Exception as e:
    print(e)
    driver.quit()
    sys.exit(1)
