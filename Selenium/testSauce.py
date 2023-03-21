from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSauce:
    def __init__(self) -> None:
        self.driver = webdriver.Safari()

    def test_invalid_login(self):
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        
        sleep(2) # We will restructure and put the different function instead of the sleep funciton in later times.

        user_name = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        
        sleep(2)

        user_name.send_keys("test")
        password.send_keys("test123")

        sleep(1)

        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_result = error_message.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Result: {test_result}, {error_message.text}")
    
    def test_login_empty(self):
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        sleep(1)
        user_name = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        sleep(1)
        user_name.send_keys("")
        password.send_keys("")
        sleep(1)
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        sleep(1)
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3/text()")
        
        test_result = error_message.text == "Epic sadface: Username is required"
        print(f"Test Result: {test_result}, {error_message.text}")
    
    def test_login_empty_password(self):
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        sleep(1)
        user_name = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        sleep(1)
        user_name.send_keys("test")
        password.send_keys("")
        sleep(2)
        login_button = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_button.click()
        sleep(1)
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_result = error_message.text == "Epic sadface: Password is required"
        print(f"Test Result: {test_result}, {error_message.text}")
    
    def test_login_locked_out(self):
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        sleep(1)
        user_name = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        sleep(1)
        user_name.send_keys("locked_out_user")
        password.send_keys("secret_sauce")
        sleep(1)
        login_button = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_button.click()
        sleep(1)
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_result = error_message.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Result: {test_result}, {error_message.text}")

    def test_login_empty_2(self):
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        sleep(1)
        user_name = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        sleep(1)
        user_name.send_keys("")
        password.send_keys("")
        sleep(1)
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        sleep(1)
        error_button = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3/button")
        error_button.click()
        sleep(2)

    def test_valid_login(self):
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        sleep(1)
        user_name = self.driver.find_element(By.ID, "user-name")
        password = self.driver.find_element(By.ID, "password")
        sleep(1)
        user_name.send_keys("standard_user")
        password.send_keys("secret_sauce")
        sleep(1)
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        sleep(3)
        list_item = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Number of Item: {len(list_item)}")

test_Class = TestSauce()
#test_Class.test_invalid_login()
#test_Class.test_login_empty()
#test_Class.test_login_empty_password()
#test_Class.test_login_locked_out()
#test_Class.test_login_empty_2()
#test_Class.test_valid_login()