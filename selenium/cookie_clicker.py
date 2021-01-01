from selenium import webdriver
import time

chrome_driver_path = 'C:/Users/Dreambuild/Desktop/Resume/chromedriver_win32/chromedriver.exe'

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 5
five_min = time.time() + 60*5
cookie = driver.find_element_by_id("cookie")

items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

while True:
    cookie.click()

    if time.time() > timeout:
        store_items = driver.find_elements_by_css_selector("#store b")
        prices = []
        for item in store_items:
            try:
                price = int(item.text.split("- ")[1].replace(",", ""))
            except:
                continue
            else:
                prices.append(price)

        cookie_upgrades = {}
        for n in range(len(prices)):
            cookie_upgrades[prices[n]] = item_ids[n]

        money = int(driver.find_element_by_id("money").text.replace(",", ""))

        affordable_upgrades = {}
        for price, id in cookie_upgrades.items():
            if money > price:
                affordable_upgrades[price] = id

        highest_affordable_item = max(affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_affordable_item]

        item_to_buy = driver.find_element_by_id(to_purchase_id)
        item_to_buy.click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break

