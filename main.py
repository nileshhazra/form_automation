from selenium import webdriver
import time

# Variables
path = 'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
web_path = 'https://docs.google.com/forms/d/e/1FAIpQLSeJVgNegjlq0IkY79KoxfY6ThtnFMI1ykZGw8thGLmu58IOtw/viewform?usp=sf_link'
name_field = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
school_field = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
number_field = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'

# Initialising webdriver for chrome
driver = webdriver.Chrome(path)

# getting the URL
driver.get(web_path)

py_input = driver.find_element_by_xpath(name_field)
time.sleep(0.1)
py_input.send_keys('Laura Palmer')

py_input = driver.find_element_by_xpath(school_field)
py_input.send_keys('Georgia Institute of technology')

py_input = driver.find_element_by_xpath(number_field)
py_input.send_keys('7488171988')

py_input = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]').click()
time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[4]').click()

time.sleep(0.1)
driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span').click()

driver.find_element_by_xpath('//*[@id="i5"]/div[3]/div').click()

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span').click()

driver.find_element_by_xpath('//*[@id="i8"]/div[3]/div').click()

driver.find_element_by_xpath('//*[@id="i30"]/div[3]/div').click()

driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div[2]/span').click()

# driver.close()

# driver.implicitly_wait(50)
# print("Element is visible? " + str(py_input.is_displayed()))
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[4]/span -- open options --running not selecting
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[4]/span --selected option --not running
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[2]/div[4] --div for option --not running
# //*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[4] --div for selected option --not running
