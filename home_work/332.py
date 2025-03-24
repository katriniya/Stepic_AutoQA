from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        welcome_text = main_test("http://suninjuly.github.io/registration1.html")
        assert "Congratulations! You have successfully registered!" == welcome_text

    def test_abs2(self):
        welcome_text = main_test("http://suninjuly.github.io/registration2.html")
        assert "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    unittest.main()


def main_test(link):
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block>.first_class>input")
    first_name.send_keys('Name')
    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block>.second_class>input")
    last_name.send_keys('Last')
    email = browser.find_element(By.CSS_SELECTOR, ".first_block>.third_class>input")
    email.send_keys('abs@123.123')

    # необязательные поля (по заданию их не надо заполнять!)
    phone = browser.find_element(By.CSS_SELECTOR, ".second_block>.first_class>input")
    address = browser.find_element(By.CSS_SELECTOR, ".second_block>.second_class>input")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    time.sleep(3)
    browser.quit()

    return (welcome_text)
