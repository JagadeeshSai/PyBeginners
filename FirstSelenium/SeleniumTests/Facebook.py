from selenium import webdriver
import unittest
from selenium.webdriver.support.select import Select
import pytest


class FbRegistration(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_FBReg(self):
        self.driver.get("https://www.facebook.com/")
        if(self.driver.find_element_by_name('firstname').is_enabled()):
            self.driver.find_element_by_name('firstname').send_keys("Jagadeesh")

        self.driver.find_element_by_name('lastname').send_keys("Ranorex")
        self.driver.find_element_by_name('reg_email__').send_keys("8050321921")
        self.driver.find_element_by_name('reg_passwd__').send_keys("080503219210")

        Select(self.driver.find_element_by_name('birthday_day')).select_by_value('10')
        Select(self.driver.find_element_by_name('birthday_month')).select_by_value('11')
        Select(self.driver.find_element_by_name('birthday_year')).select_by_value('2008')
        try:
            if (self.driver.find_element_by_xpath('//*[@id="u_0_6"]').is_enabled()):
                rdoMale = self.driver.find_element_by_xpath('//*[@id="u_0_6"]')
                rdoMale.click()
                if (rdoMale.is_selected()):
                    print("Male Radio Button Clicked")
                else:
                    print("Male Radio Button Not Clicked")
            else:
                print("Male Radio Button Not Found")
        except:
            print("Male Radio Button Issue -- Except")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()