import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

# from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path='../drivers/chromedriver.exe')
driver.get("https://www.hdfcergo.com/")
driver.maximize_window()



driver.find_element_by_xpath("//*[@id='menu-slider-carousel']/div/div[5]/a/i").click()
driver.find_element_by_xpath("//*[@id='car-homepage']/div[2]/div/div[2]/button").click()

driver.minimize_window()
driver.maximize_window()
driver.implicitly_wait(30)
# time.sleep(30)

element = driver.find_element_by_css_selector("#hdnOwnershipName")  # //span[@id='HomeCoverSpan']/../../div[1]
# element.send_keys('A Home Owner')
driver.execute_script("arguments[0].value = 'A Home Owner'", element)

# driver.find_element_by_xpath("//span[@id='7']").click()


# driver.find_element_by_xpath("//*[@id='HomeCoverSpan']").click()
# driver.find_element_by_xpath("//*[@id='RiskCoverSpan']").click()
# driver.find_element_by_xpath("//*[@id='car-homepage']/div/div/div/div[2]/div/div/button").click()