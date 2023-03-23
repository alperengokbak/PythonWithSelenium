from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestSauce:
    def __init__(self) -> None:
        self.driver = webdriver.Safari()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        sleep(1) # We will restructure and put the different function instead of the sleep funciton in later times.
        self.user_name = self.driver.find_element(By.ID, "user-name")
        self.password = self.driver.find_element(By.ID, "password")
        sleep(1)

    def test_invalid_login(self):
        self.user_name.send_keys("test")
        self.password.send_keys("test123")
        sleep(1)
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_result = error_message.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"Test Result: {test_result}, {error_message.text}")
    
    def test_login_empty(self):
        self.user_name.send_keys("")
        self.password.send_keys("")
        sleep(1)
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3/text()")
        
        test_result = error_message.text == "Epic sadface: Username is required"
        print(f"Test Result: {test_result}, {error_message.text}")
    
    def test_login_empty_password(self):
        self.user_name.send_keys("test")
        self.password.send_keys("")
        sleep(2)
        login_button = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_button.click()
        
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_result = error_message.text == "Epic sadface: Password is required"
        print(f"Test Result: {test_result}, {error_message.text}")
    
    def test_login_locked_out(self):
        self.user_name.send_keys("locked_out_user")
        self.password.send_keys("secret_sauce")
        sleep(1)
        login_button = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_button.click()
        
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        test_result = error_message.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Result: {test_result}, {error_message.text}")

    def test_login_empty_2(self):
        self.user_name.send_keys("")
        self.password.send_keys("")
        sleep(1)
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        sleep(1)
        error_button = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3/button")
        error_button.click()
        sleep(2)

    def test_valid_login(self):
        self.user_name.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        sleep(1)
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        sleep(2)
        list_item = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Number of Item: {len(list_item)}")
    
    def test_add_product(self):
        self.user_name.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        sleep(1)
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        sleep(1)
        click_button = self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
        click_button.click()
        sleep(1)
        cart_button = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_button.click()
        sleep(1)
        test_cart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        test_result = int(test_cart.text) > 0
        print(f"Test Result: {test_result}, Product count: {test_cart.text}")
        
    def test_remove_product(self):
        self.user_name.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        sleep(1)
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        sleep(1)
        add_button = self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-bike-light']")
        add_button.click()
        sleep(1)
        #add_button = self.driver.find_element(By.XPATH, "//*[@id='add-to-cart-sauce-labs-fleece-jacket']")
        #add_button.click()
        #sleep(1)
        test_cart = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        test_cart.click()
        sleep(1)
        remove_button = self.driver.find_element(By.ID, "remove-sauce-labs-bike-light")
        remove_button.click()
        sleep(1)
        cart_item_count = self.driver.find_elements(By.CLASS_NAME, "cart_item")
        try: 
            for element in cart_item_count:
                print(element)
        except Exception as e:
            print(e)

        test_result = cart_item_count == []
        if test_result:
            print(f"Test Result: {test_result}, Removed succesfully the whole products.")
        else:
            print(f"Test Result: {test_result}, The whole product did not remove from the cart.")

    def test_take_price_list(self):
        self.user_name.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        sleep(1)
        login_btn = self.driver.find_element(By.CLASS_NAME, "submit-button")
        login_btn.click()
        sleep(1)
        my_list = list()
        limit = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        width = self.driver.execute_script("return arguments[0].offsetWidth", limit) # We can take the size of defined value with that function.
        
        for element in limit:
            my_list.append(float(element.text[1 : width]))
        print(my_list)


test_Class = TestSauce()
#test_Class.test_invalid_login()
#test_Class.test_login_empty()
#test_Class.test_login_empty_password()
#test_Class.test_login_locked_out()
#test_Class.test_login_empty_2()
#test_Class.test_valid_login()
#test_Class.test_add_product()
test_Class.test_remove_product()
#test_Class.test_take_price_list()