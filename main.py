from selenium import webdriver
from selenium.webdriver.support.ui import Select



driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')

driver.get('https://docs.google.com/forms/d/e/1FAIpQLSeJVgNegjlq0IkY79KoxfY6ThtnFMI1ykZGw8thGLmu58IOtw/viewform?usp=sf_link')

py_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
py_input.send_keys('Nilesh Hazra')
py_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
py_input.send_keys('Birla Institute of technology , Mesra')
py_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
py_input.send_keys('7488172988')

py_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]').click()
driver.implicitly_wait(10)
py_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[4]').click()

py_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()
driver.implicitly_wait(10)
py_input = driver.find_element_by_xpath('//*[@id="i5"]/div[3]/div').click()

py_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span').click()

py_input = driver.find_element_by_xpath('//*[@id="i8"]/div[3]/div').click()
py_input = driver.find_element_by_xpath('//*[@id="i30"]/div[3]/div').click()

py_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span').click()









# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[4]/span -- open options --running not selecting
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[4]/span --selected option --not running
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[4] --div for option --not running
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[4] --div for selected option --not running


