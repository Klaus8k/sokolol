import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

os.environ['PATH'] += r";C:/Selenium_drivers"

driver = webdriver.Chrome()
driver.get(r'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html')
WebDriverWait(driver, timeout = 5)
btn = driver.find_element(By.ID, 'downloadButton')
btn.click()