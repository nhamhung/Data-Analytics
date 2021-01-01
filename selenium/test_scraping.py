from selenium import webdriver
from datetime import datetime

chrome_driver_path = 'C:/Users/Dreambuild/Desktop/Resume/chromedriver_win32/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver_path);

driver.get("https://www.python.org/")

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for i in range(len(event_names)):
    events[i] = {
        "time": event_times[i].text,
        "name": event_names[i].text
    }

print(events)

driver.close()