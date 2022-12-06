import os
import getpass
from pyvirtualdisplay import Display

import logging


from selenium import webdriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

# from .constants import url_m_grup

logging.basicConfig(level=logging.WARNING, filename='log_parser.txt')


url_m_grup = r'https://gmprint.ru/calc/leaflets'

target_url = url_m_grup


class Parse_unit(webdriver.Firefox):
    def __init__(self):
        # Check the system and add path and driver options
        if os.name == 'posix':
            os.environ['PATH'] += f":/home/{getpass.getuser()}/www/Selenium_drivers"
            self.run_in_xvfb()
            super(Parse_unit, self).__init__()
            logging.warning('------------------->' + os.environ['PATH'])
        else:
            os.environ['PATH'] += r";C:/Selenium_drivers"
            options = Options()
            options.page_load_strategy = 'normal'
            # options.headless = True
            options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
            super(Parse_unit, self).__init__(options=options)

    def run_in_xvfb(self):
        self.display = Display(visible=False)
        self.display.start()

    def land_first_page(self):
        self.get(target_url)
        print(self.title)

    def click_on_element(self, element: object):
        self.execute_script("arguments[0].click();", element)

    def __del__(self):  # stop display if on linux, and quit from webdriver
        if self.__dict__['caps']['platformName'] != 'windows':
            self.display.stop()
        self.quit()


# TODO из объекта заказа берем данные по заказу

def parce_m_grup(offset_obj: dict):

    density_order = int(offset_obj['weigh'])
    formatX = offset_obj['width']
    formatY = offset_obj['higth']
    color_duplex = False # offset_obj.__dict__['dublicate']
    pressrun = offset_obj['order']

    with Parse_unit() as m_grup:

        # Главная страница
        m_grup.land_first_page()

        m_grup.implicitly_wait(10)


        # Проверка города
        m_grup.find_element(By.ID, 'its_my_city').click()

        # Переход в меню листовок
        btn_leaflets = m_grup.find_element(By.CLASS_NAME, 'menu_leaflets')
        m_grup.click_on_element(btn_leaflets)

        # Выбор 4+4 или 4+0
        # TODO Кликает через раз.
        # a = m_grup.find_element(
        #     By.CSS_SELECTOR, 'span[aria-labelledby^="select2-color"]')
        # a.click()
        # b = m_grup.find_element(By.CSS_SELECTOR, 'ul[id^="select2-color"]')

        # duplex_list = b.find_elements(
        #     By.CSS_SELECTOR, 'li[role="option"]')

        # for i in duplex_list:
        #     if color_duplex == True and i.text == 'С двух сторон':
                
        #         btn_duplex = i
        #         break
        #     elif color_duplex == False and i.text == 'С одной стороны':
        #         btn_duplex = i
        #         break
        # btn_duplex.click()

        # Выбор бумаги
        m_grup.find_element(
            By.CSS_SELECTOR, 'span[id^="select2-density"]').click()
        choise_density = m_grup.find_element(By.CSS_SELECTOR, 'ul[id^="select2-density"]')
        density_list = choise_density.find_elements(
            By.CSS_SELECTOR, 'li[role="option"]')

        for i in density_list:
            if i.text.startswith(str(density_order)):
                density_paper = i
                break
        density_paper.click()

        # Установка формата изделия
        other_format = m_grup.find_element(By.ID, 'other_format_button')
        other_format.click()
        x = m_grup.find_element(
            By.CSS_SELECTOR, 'input[name="formatX"]')
        y = m_grup.find_element(
            By.CSS_SELECTOR, 'input[name="formatY"]')
        x.send_keys(formatX)
        y.send_keys(formatY)

        # Установка своего тиража
        other_pressrun = m_grup.find_element(By.ID, 'other_circul_button')
        other_pressrun.click()
        x = m_grup.find_element(
            By.CSS_SELECTOR, 'input[name="circulation_other"]')
        x.clear()
        x.send_keys(pressrun)

        # Итоговая цена тиража
        WebDriverWait(m_grup, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'span[class="b-price__text"')))
        

        print('result ------->', m_grup.find_element(By.CSS_SELECTOR,
                'span[class="b-price__text"').text)
        return(m_grup.find_element(By.CSS_SELECTOR,
                'span[class="b-price__text"').text)

