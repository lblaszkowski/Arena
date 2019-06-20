import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

szukanie_sport = "Sport"
url = 'https://buggy-testingcup.pgs-soft.com/'


class zadanieDrugie(unittest.TestCase):

    def setUp(self, browser="chrome"):
        if browser == "chrome":
            self.driver = webdriver.Chrome(executable_path=r'../Drivers/ChromeDrive_74/chromedriver.exe')
            self.driver.maximize_window()
            self.driver.get(url + 'task_2')
        elif browser == "mozilla":
            self.driver = webdriver.Firefox(executable_path=r'../Drivers/FirefoxDrive_24/geckodriver.exe')
            self.driver.maximize_window()
            self.driver.get(url + 'task_2')
        else:
            print("Brak przeglądarki")
            raise Exception("Brak przeglądarki")
        return self.driver


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_WybranieDowolnegoProduktu(self):
        driver = self.driver
        element = driver.find_element_by_xpath("//span[contains(@class,'placeholder')]")
        element.click()
        element1 = driver.find_element_by_xpath("//input[@autocorrect='off']")
        element1.send_keys(szukanie_sport)
        element1.send_keys(Keys.ENTER)
        sleep(3)

        # element = Select(driver.find_element_by_class_name("js-category-select select2-hidden-accessible"))
        # # element = Select(driver.find_element_by_xpath("//span[@title='Sport']"))
        # # element.select_by_value("Sport")
        # # element.select_by_index(1)
        # element.select_by_visible_text("Sport")
        # element.click()
        # sleep(10)

