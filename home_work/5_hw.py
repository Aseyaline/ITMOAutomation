# Создайте файл 5_hw.py в нем выполняйте все задания
# 1. Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
# i. текстовое поле username
# ii. текстовое поле password
# iii. кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

elem = driver.find_elements(By.CSS_SELECTOR, "#user-name, #password, #login-button")
if len(elem) == 3:
    print('Элементы найдены')
else:
    print('Элементы не найдены')


# 2. CSS - Перейдите на тренировочную площадку, решите до 14-го задания включительно
# a. https://flukeout.github.io/
