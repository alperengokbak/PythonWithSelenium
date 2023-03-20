from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

driver.maximize_window()  # That command will maximize the website screen.
driver.get("https://www.google.com/")

sleep(1)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Kodlama.io")

sleep(1)

search_button = driver.find_element(By.NAME, "btnK")
search_button.click()

sleep(1)

first_result = driver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/h3")
first_result.click()

sleep(1)

# Important! "find_element" return just a variable, but "find_elements" is returning the variable type of list.
listOfCourses = driver.find_elements(By.CLASS_NAME, "course-listing")
print(f"Number of instruction in Kodlama.io: {len(listOfCourses)}")

sleep(3)