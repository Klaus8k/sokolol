import os

from pyvirtualdisplay import Display

import logging


from selenium import webdriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from constants import *

# logging.basicConfig(level=logging.WARNING)

target_url = url_m_grup


class Parse_unit(webdriver.Firefox):
    def __init__(self):
        # Check the system and add path and driver options
        if os.name == 'posix':
            os.environ['PATH'] += f":/home/{os.getlogin()}/www/Selenium_drivers"
            self.run_in_xvfb()
            super(Parse_unit, self).__init__()
        else:
            os.environ['PATH'] += r";C:/Selenium_drivers"
            options = Options()
            # options.headless = True
            options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
            super(Parse_unit, self).__init__(options=options)

    def run_in_xvfb(self):
        self.display = Display(visible=False)
        self.display.start()

    def land_first_page(self):
        self.get(target_url)
        print(self.title)

    def __del__(self):  # stop display if on linux, and quit from webdriver
        if self.__dict__['caps']['platformName'] != 'windows':
            self.display.stop()
        self.quit()


if __name__ == '__main__':
    def parce_m_grup(options=''):
        with Parse_unit() as m_grup:
            m_grup.land_first_page()
            m_grup.find_element(By.ID, 'its_my_city').click()
 
# TODO js hack method, bug. Must be search other way

            btn_leaflets = m_grup.find_element(By.CLASS_NAME, 'menu_leaflets')
            print(btn_leaflets.is_enabled())
            m_grup.execute_script("arguments[0].click();", btn_leaflets)
            # btn_leaflets.click()

            # element = WebDriverWait(m_grup, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, 'menu_leaflets')))
            # m_grup.execute_script("arguments[0].click();", element)

            

            m_grup.find_element(By.CSS_SELECTOR, 'span[id^="select2-density"]').click()
            destiny = m_grup.find_element(By.CLASS_NAME, 'select2-results__options')
            destiny_list = destiny.find_elements(By.CSS_SELECTOR, 'li[role="option"]')

            x = None
            for i in destiny_list:
                if i.text == '170 г/м² бумага глянц.':
                    x = i
                    break
            
            x.click()
            

            other_format = m_grup.find_element(By.ID, 'other_format_button')
            other_format.click()
            m_grup.find_element(By.CSS_SELECTOR, 'input[name="formatX"]').send_keys(100)
            m_grup.find_element(By.CSS_SELECTOR, 'input[name="formatY"]').send_keys(100)
            m_grup.implicitly_wait(10)
# TODO УСЛОВНОЕ ОЖИДАНИЕ ДЛЯ РЕЗУЛЬТАТА, ВОЗМОЖНА ПРОКРУТКА НУЖНА
            result = WebDriverWait(m_grup, 20).until(
                EC.text_to_be_present_in_element((
                By.CLASS_NAME, 'b-price__text')))

            print(result)
                    

    parce_m_grup()
