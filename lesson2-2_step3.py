from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    num1_element = browser.find_element_by_css_selector("#num1")
    num1 = num1_element.text
    num2_element = browser.find_element_by_css_selector("#num2")
    num2 = num2_element.text

    select = Select(browser.find_element_by_css_selector("#dropdown"))
    select.select_by_visible_text(str(int(num1) + int(num2)))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
