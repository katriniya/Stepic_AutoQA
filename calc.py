from selenium.webdriver.common.by import By
import math
import time

def calc_math(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def main(browser):
  x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
  z= calc_math(x)
  input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
  input_answer.send_keys(z)

  button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
  button.click()

  time.sleep(10)
  browser.quit()
