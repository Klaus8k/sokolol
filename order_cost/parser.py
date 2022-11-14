import os
from selenium import webdriver
from selenium.webdriver.common.by import By

os.environ['PATH'] += r";C:/Selenium_drivers"

driver = webdriver.Chrome()
driver.get(r'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')
btn = driver.find_element(By.ID, 'downloadButton')
