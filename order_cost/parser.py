import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--ignore-certificate-errors')
os.environ['PATH'] += r";C:/Selenium_drivers"

driver = webdriver.Chrome(options=options)
driver.get(r'https://gmprint.ru/')
driver.implicitly_wait(3)
btn = driver.find_element(By.ID, 'its_my_city')
btn.click()
nextt = driver.find_element(By.LINK_TEXT, 'Визитки')
nextt.click()
print(driver.current_url)




