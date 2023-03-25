from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from pathlib import Path
from datetime import date
import pytest

# 3A --> Act, Arrange, Assert
class Test_Demo:
    # Will call before each test.
    def setup_method(self): 
        self.driver = webdriver.Safari()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        self.wait_for_element_visible((By.ID, "user-name"))
        self.user_name = self.driver.find_element(By.ID, "user-name")
        self.wait_for_element_visible((By.ID, "password"))
        self.password = self.driver.find_element(By.ID, "password")

        # Take the date of today and check is there any file if there is not, create.
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    # Will call after each test.
    def teardown_method(self):
        self.driver.quit()
    
    def wait_for_element_visible(self, locator, timeout = 5):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
    
    def wait_for_element_clickable(self, locator, timeout = 5):
        WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def create_action_chain(self, username, password):
        valid_login = ActionChains(self.driver)
        valid_login.send_keys_to_element(self.user_name, username)
        valid_login.send_keys_to_element(self.password, password)
        valid_login.perform()

    def test_valid_login(self):
        self.create_action_chain("standard_user", "secret_sauce")
        self.wait_for_element_clickable((By.CLASS_NAME, "submit-button"))
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        list_item = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(self.folderPath + "/test-valid-login.png")
        assert len(list_item) == 6
    
    def test_invalid_login(self):
        self.create_action_chain("test", "test123")
        self.wait_for_element_clickable((By.CLASS_NAME, "submit-button"))
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        self.wait_for_element_visible((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3"))
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(self.folderPath + f"/test-invalid-login.png")
        assert error_message.text == "Epic sadface: Username and password do not match any user in this service"
    
    def test_login_empty(self):
        self.create_action_chain("","")
        self.wait_for_element_clickable((By.CLASS_NAME, "submit-button"))
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3/text()")
        self.driver.save_screenshot(self.folderPath + "/test-login-empty.png")
        assert error_message.text == "Epic sadface: Username is required"

    def test_login_empty_password(self):
        self.create_action_chain("test", "")
        self.wait_for_element_clickable((By.CLASS_NAME, "submit-button"))
        login_button = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_button.click()
        self.wait_for_element_visible((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3"))
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert error_message.text == "Epic sadface: Password is required"
    
    def test_login_locked_out(self):
        self.create_action_chain("locked_out_user", "secret_sauce")
        self.wait_for_element_clickable((By.CLASS_NAME, "submit-button"))
        login_button = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_button.click()
        self.wait_for_element_visible((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3"))
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        assert error_message.text == "Epic sadface: Sorry, this user has been locked out."

    def test_login_empty_2(self):
        self.create_action_chain("", "")
        self.wait_for_element_clickable((By.CLASS_NAME, "submit-button"))
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        self.wait_for_element_visible((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3/button"))
        error_button = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3/button")
        error_button.click()
        assert True