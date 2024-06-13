import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

url = "https://www.divan.ru/novosibirsk/category/potolocnye-svetilniki"

driver.get(url)

time.sleep(3)

svetilniki = driver.find_elements(By.CLASS_NAME, 'div._Ud0k')

parsed_data = []

for svetilnik in svetilniki:

    name = svetilnik.find_element(By.CLASS_NAME, 'div.lsooF')
    price = svetilnik.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU')
    url = svetilnik.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8').get_attribute('href')

    parsed_data.append([name, price, url])

driver.quit()

with open("sunlithe.csv", 'w', newline='', encoding='utf-8') as file:

    writer = csv.writer(file)

    writer.writerow(['название', 'цена', 'ссыла'])

    writer.writerows(parsed_data)