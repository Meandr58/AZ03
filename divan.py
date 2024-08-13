from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# Путь к веб-драйверу Firefox
driver = webdriver.Firefox()

# Открываем сайт
url = 'https://www.divan.ru/category/pramye-divany'
driver.get(url)
time.sleep(15)

# Парсинг цен
price_elements = driver.find_elements(By.XPATH, "//span[@data-testid='price']")

# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in price_elements:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()
print("Цены сохранены в файл prices.csv")
