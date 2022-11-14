import os
from selenium import webdriver

os.environ['PATH'] += r";C:\Selenium_drivers"
print('-----------------',os.environ.get('PATH'), '-----------------')

driver = webdriver.Chrome()
