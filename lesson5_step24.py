from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from calc import main


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 1200).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100" )
    )
button = browser.find_element(By.CSS_SELECTOR, "button#book")
button.click()

main(browser)
