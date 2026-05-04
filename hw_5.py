from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def task_1():
    """
    1. Переходит на страницу https://www.saucedemo.com/
    2. Находит элементы: username, password, submit button
    3. Выводит "Элементы найдены", если все элементы найдены
    """

    driver = webdriver.Chrome()

    try:
        # Переходим на страницу
        driver.get("https://www.saucedemo.com/")

        # Небольшая пауза для загрузки страницы
        # time.sleep(2)

        # Находим элементы
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.ID, "login-button")

        # Проверяем элементы
        if username_field and password_field and submit_button:
            print("Элементы найдены")

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        driver.quit()

# Запуск функции
if __name__ == "__main__":
    task_1()