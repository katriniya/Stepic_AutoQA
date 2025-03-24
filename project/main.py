from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    link_2 = "https://suninjuly.github.io/registration2.html" #ссылка для проверки ошибки
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block>.first_class>input")
    first_name.send_keys('Name')
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block>.second_class>input")
    last_name.send_keys('Last')
    email = browser.find_element(By.CSS_SELECTOR, ".first_block>.third_class>input")
    email.send_keys('abs@123.123')

    #необязательные поля (по заданию их не надо заполнять!)
    phone = browser.find_element(By.CSS_SELECTOR, ".second_block>.first_class>input")
    address = browser.find_element(By.CSS_SELECTOR, ".second_block>.second_class>input")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()