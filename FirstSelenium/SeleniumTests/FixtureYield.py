from selenium import webdriver
from selenium.webdriver.support.select import Select
import pytest

# Execute like 'pytest FixtureYield.py' in 'Terminal' by right click on this and select 'Open Terminal'

@pytest.fixture()
def env_setup():
    global driver
    driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()

def test_FBReg(env_setup):
    driver.get("https://www.facebook.com/")
    if(driver.find_element_by_name('firstname').is_enabled()):
        driver.find_element_by_name('firstname').send_keys("Jagadeesh")

    driver.find_element_by_name('lastname').send_keys("Ranorex")
    driver.find_element_by_name('reg_email__').send_keys("8050321921")
    driver.find_element_by_name('reg_passwd__').send_keys("080503219210")

    Select(driver.find_element_by_name('birthday_day')).select_by_value('10')
    Select(driver.find_element_by_name('birthday_month')).select_by_value('11')
    Select(driver.find_element_by_name('birthday_year')).select_by_value('2008')
    try:
        if (driver.find_element_by_xpath('//*[@id="u_0_6"]').is_enabled()):
            rdoMale = driver.find_element_by_xpath('//*[@id="u_0_6"]')
            rdoMale.click()
            if (rdoMale.is_selected()):
                print("Male Radio Button Clicked")
            else:
                print("Male Radio Button Not Clicked")
        else:
            print("Male Radio Button Not Found")
    except:
        print("Male Radio Button Issue -- Except")


