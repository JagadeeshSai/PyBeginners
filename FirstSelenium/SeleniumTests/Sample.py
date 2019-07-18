from selenium import webdriver
import unittest
import time
# import HtmlTestRunner

class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_automationstepbystep(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Pyhon Selenium Training")
        self.driver.find_element_by_name("btnK").click()

    # @unittest.skip("This is a skipped test.")
    # def test_search_raghav(self):
    #     self.driver.get("https://google.com")
    #     self.driver.find_element_by_name("q").send_keys("Cignti")
    #     self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
    unittest.main() # testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Administrator/PycharmProjects/Selenium/reports')