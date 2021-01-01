from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:/Users/Dreambuild/Desktop/Resume/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element_by_name("fName")
first_name.send_keys("Quoc Hung")

last_name = driver.find_element_by_name("lName")
last_name.send_keys("Nham")

email = driver.find_element_by_name("email")
email.send_keys("nhamhung.gttn@gmail.com")

sign_up = driver.find_element_by_tag_name("button")
sign_up.click()

driver.quit()