from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSauce:
    def test_invalid_login(self):
        driver = webdriver.Safari()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com")
        
        sleep(2) # We will restructure and put the different function instead of the sleep funciton in later times.

        user_name = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        
        sleep(2)

        user_name.send_keys("test")
        password.send_keys("test123")

        sleep(1)

        login_btn = driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        
        error_message = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_result = error_message.text == 'Epic sadface: Username and password do not match any user in this service'
        print(f"Test Result: {test_result}")

test_Class = TestSauce()
test_Class.test_invalid_login()
