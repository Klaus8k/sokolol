import os
from selenium import webdriver

print(os.pathsep)
os.environ['PATH'] += r";C:/Selenium_drivers"

print('-----------------',os.environ.get('PATH'), '-----------------')

driver = webdriver.Chrome()
