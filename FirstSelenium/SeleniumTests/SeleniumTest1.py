from selenium import webdriver
import unittest
import time

class GogleSrchCls(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    # @unittest.skip("This is a skipped test.")
    def test_TypeTest1(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Pyhon Selenium Training")
        self.driver.find_element_by_name("btnK").click()

    def test_TypeTest2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Pyhon Selenium Training")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main()