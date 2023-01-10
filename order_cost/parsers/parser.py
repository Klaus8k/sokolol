import os
import pathlib
import getpass
from pyvirtualdisplay import Display

from my_logger import logger_parser as logger

from selenium import webdriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

url_m_grup = r'https://gmprint.ru/calc/leaflets'

target_url = url_m_grup


class Parse_unit(webdriver.Firefox):
    def __init__(self):
        # Check the system and add path and driver options
        if os.name == 'posix':
            os.environ['PATH'] += ':' + \
                str(pathlib.Path.home() / 'www/Selenium_drivers/')
            # logger.warning(f'{os.environ["PATH"]}')
            self.run_in_xvfb()
            super(Parse_unit, self).__init__(
                service_log_path='logs/geckodriver_log.txt')
        else:
            os.environ['PATH'] += r";C:\Selenium_drivers"
            # logger.warning(f'{os.environ["PATH"]}')
            options = Options()
            options.page_load_strategy = 'normal'
            options.headless = True
            options.binary_location = r'C:/Program Files/Mozilla Firefox/firefox.exe'
            super(Parse_unit, self).__init__(options=options,
                                             service_log_path='logs/geckodriver_log.txt')

    def run_in_xvfb(self):
        self.display = Display(visible=False)
        self.display.start()

    def land_first_page(self):
        self.get(target_url)

    def click_on_element(self, element: object):
        self.execute_script("arguments[0].click();", element)

    def __del__(self):  # stop display if on linux, and quit from webdriver
        if os.name == 'posix':
        # if self.__dict__['caps']['platformName'] != 'windows':
            self.display.stop()
        self.quit()


def parce_m_grup(offset_obj: object):
    logger.warning('Start parse m_grup')
    logger.warning('input params - %s', offset_obj)
    # из объекта заказа берем данные по заказу словарем

    density = offset_obj['density']
    formatX = offset_obj['formatX']
    formatY = offset_obj['formatY']
    # offset_obj.__dict__['duplex'] --- TODO выбор дуплекса не работет!
    duplex = False
    pressrun = offset_obj['pressrun']

    with Parse_unit() as m_grup:

        # Главная страница
        m_grup.land_first_page()
        m_grup.implicitly_wait(10)

        # Проверка города TODO проверить, или по обычному ищем и кликаем на город.
        # Но возможно надо переключить окно на всплывающее

        # m_grup.find_element(By.ID, 'change_city').click()
        # city_menu = m_grup.find_element(By.CLASS_NAME, 'b-popup')
        # city_list = city_menu.find_elements(
        #     By.CSS_SELECTOR, 'li[class="b-list__item"]')

        # for i in city_list:
        #     i.find_element(By.CSS_SELECTOR,
        #                    'a[data-city_name="Москва"]').click()

        m_grup.find_element(By.ID, 'its_my_city').click()

        # Переход в меню листовок
        btn_leaflets = m_grup.find_element(By.CLASS_NAME, 'menu_leaflets')
        m_grup.click_on_element(btn_leaflets)

        # Выбор 4+4 или 4+0
        # TODO Кликает через раз.
        # a = m_grup.find_element(
        #     By.CSS_SELECTOR, 'span[aria-labelledby^="select2-color"]')
        # logging.warning('-------------------------------->>>>')
        # WebDriverWait(m_grup, 10).until(EC.element_to_be_clickable(a))
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
        choise_density = m_grup.find_element(
            By.CSS_SELECTOR, 'ul[id^="select2-density"]')
        density_list = choise_density.find_elements(
            By.CSS_SELECTOR, 'li[role="option"]')

        for i in density_list:
            if i.text.startswith(str(density)):
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

        # Итоговая цена тиража - TODO не всегда результат отдает
        WebDriverWait(m_grup, 20).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'span[class="b-price__text"')))
        result = m_grup.find_element(By.CSS_SELECTOR,
                                     'span[class="b-price__text"').text
        logger.warning('result - %s', result)
        del(m_grup)

        return result
