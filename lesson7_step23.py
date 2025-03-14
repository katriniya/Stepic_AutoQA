from selenium import webdriver
from selenium.webdriver.common.by import By
from calc import main


browser = webdriver.Chrome()
browser.implicitly_wait(5)
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
button.click()

browser.switch_to.window(browser.window_handles[1])

main(browser)
