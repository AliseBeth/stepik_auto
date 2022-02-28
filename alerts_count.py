
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    button = WebDriverWait(browser, 5). until(
        expected_conditions.text_to_be_present_in_element((By.ID, 'price'), u'100')
    )
    button.click()

    def count(x):
        return str(math.log(abs(12 * math.sin(x))))

    x = browser.find_element(By.ID, 'input_value').text
    math_x = int(x)
    final = count(math_x)

    place = browser.find_element(By.ID, 'answer')
    place.send_keys(final)

    submit = browser.find_element(By.CLASS_NAME, 'btn')
    submit.click()

    time.sleep(5)
finally:
    browser.quit()