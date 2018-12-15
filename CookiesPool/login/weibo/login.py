

import random
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
url='https://weibo.com'


class Login():
    def __init__(self,browser,username='',password='',timeout=20):
        self.__timeout = timeout
        self.__browser = browser
        self.__un=username
        self.__pwd=password
        self.__browser.set_page_load_timeout(self.__timeout)
        self.__wait = WebDriverWait(self.__browser, self.__timeout)

    def login(self):
        try:
            self.__browser.get(url)
            self.__browser.delete_all_cookies()
            time.sleep(12)
            input = self.__wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#loginname')))
            for key in self.__un:
                input.send_keys(key)
                time.sleep(random.randint(0,3))
            input = self.__wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.password > div:nth-child(1) > input:nth-child(1)')))
            for key in self.__pwd:
                input.send_keys(key)
                time.sleep(random.randint(0,3))
            submit=self.__wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'div.info_list:nth-child(6) > a:nth-child(1)')))
            submit.click()
            time.sleep(3)
            return self.__browser.get_cookies()

        except TimeoutException:
            print('timeout')


if __name__=='__main__':
    ob=Login().login()


