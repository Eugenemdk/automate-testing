from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

try:
    link="http://suninjuly.github.io/explicit_wait2.html"
    browser=webdriver.Chrome()
    browser.get(link)

    wait_btn=WebDriverWait(browser,12).until(
        EC.text_to_be_present_in_element((By.XPATH,'//h5[@id="price"]'),"$100")
    )
    button_first=browser.find_element(By.XPATH,'//button[@id="book"]')
    button_first.click()
    #define and locate second button 
    button_second=browser.find_element(By.XPATH,'//button[@id="solve"]')
    #scroll down the page
    browser.execute_script("return arguments[0].scrollIntoView(true);",button_second)
    #calc the x value
    x_element=int(browser.find_element(By.XPATH,'//span[@id="input_value"]').text)
    x_value=str(math.log(abs(12*math.sin(x_element))))
    #fill the answer textfield
    textfield=browser.find_element(By.XPATH,'//input[@id="answer"]')
    textfield.send_keys(x_value)
    #submit the answer
    button_second.click()
finally:
    time.sleep(15)
    browser.quit()
