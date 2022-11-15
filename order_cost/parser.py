import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

os.environ['PATH'] += r";C:/Selenium_drivers"
target_url = r'https://gmprint.ru/'

options = Options()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

driver.get(target_url)

def press_btn(driver, id : str):
    driver.implicitly_wait(3)
    btn = driver.find_element(By.ID, id)
    btn.click()


if __name__ == '__main__':
    start = 'its_my_city'

    press_btn(driver=driver, id=start)




