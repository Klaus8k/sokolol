import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# os.environ['PATH'] += r";C:/Selenium_drivers"
os.environ['PATH'] += r":/home/klaus8/www/Selenium_drivers"

# target_url = r'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'
target_url = r'https://demo.seleniumeasy.com/basic-first-form-demo.html'

options = Options()
# options.add_argument('--ignore-certificate-errors-spki-list')
# options.add_argument('--ignore-ssl-errors')
driver = webdriver.Firefox()

driver.get(target_url)


# def press_btn(target: str, driver=driver):
#     driver.implicitly_wait(3)
#     btn = driver.find_element(By.ID, target)
#     btn.click()

# # Возвращает ссылку на объкт драйвера, отбор по ИД
# def id_ex_select(driver: driver, id: str):
#     result = WebDriverWait(driver, 30).until(lambda d: d.find_element(By.ID, id))
#     return result




if __name__ == '__main__':
    sum1 = driver.find_element(By.ID, 'sum1')
    sum2 = driver.find_element(By.ID, 'sum2')
    driver.implicitly_wait(6)
    sum1.send_keys(Keys.NUMPAD4, Keys.NUMPAD4)
    sum2.send_keys(1651)

    btn = driver.find_element(By.CSS_SELECTOR, 'button[onclick="return total()"]').click()

    print(driver.find_element(By.ID, 'displayvalue').text)
    