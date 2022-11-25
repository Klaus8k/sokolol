import os

from pyvirtualdisplay import Display

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from constants import base_url

target_url = base_url


class Parse_unit(webdriver.Firefox):
    def __init__(self):
        # Check the system and add path and driver options
        if os.name == 'posix':
            os.environ['PATH'] += f":/home/{os.getlogin()}/www/Selenium_drivers"
            with Display(visible=False, backend='xvfb') as disp:
                super(Parse_unit, self).__init__()
        else:
            os.environ['PATH'] += r";C:/Selenium_drivers"
            options=Options()
            options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
            super(Parse_unit, self).__init__(options = options)

        

    def land_first_page(self):
        self.get(target_url)






if __name__ == '__main__':
    def parce(options = ''):
        m_grup = Parse_unit()
        m_grup.land_first_page()

    parce()