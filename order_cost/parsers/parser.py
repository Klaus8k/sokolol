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

logging.basicConfig(level=logging.WARNING)

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
            options.headless = True
            options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
            super(Parse_unit, self).__init__(options=options)

    def run_in_xvfb(self):
        self.display = Display(visible=False, backend='xvfb')
        self.display.start()

    def land_first_page(self):
        self.get(target_url)
        logging.error(self.title)

    def __del__(self):  # stop display if on linux, and quit from webdriver
        if self.__dict__['caps']['platformName'] != 'windows':
            self.display.stop()
        self.quit()


if __name__ == '__main__':
    def parce_m_grup(options=''):
        with Parse_unit() as m_grup:
            m_grup.land_first_page()
            m_grup.find_element(By.ID, 'its_my_city').click()
            m_grup.find_element(By.CLASS_NAME, 'menu_leaflets').click()

            m_grup.find_element(By.CSS_SELECTOR, 'span[id^="select2-density"]').click()
            destiny = m_grup.find_element(By.CLASS_NAME, 'select2-results__options')
            destiny_list = destiny.find_elements(By.CSS_SELECTOR, 'li[role="option"]')
            print([i.text for i in destiny_list])
        




                    

    parce_m_grup()
