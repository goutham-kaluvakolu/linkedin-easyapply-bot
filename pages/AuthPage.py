from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import USER_NAME 
from config import PWD 


class AuthPage:
    def __init__(self, driver):
        self.driver = driver

    def authenticate(self):
        try:
            self.enter_auth_page()
            self.fill_email()
            self.fill_password()
            self.click_signin()
    
        except Exception as e:
            print(f"Error authenticate: {str(e)}")

    def enter_auth_page(self):
        try:
            sign_in_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Sign in')]"))
            )
            sign_in_button.click()
    
        except Exception as e:
            print(f"Error enter_auth_page: {str(e)}")

    def fill_email(self):
        try:
            # Find the username input field by its 'id' attribute
            username_input = self.driver.find_element(By.ID, "username")
            print("Username input field found:", username_input)
            
            # Enter a username into the input field
            username_input.send_keys(USER_NAME)

            time.sleep(2)

        except Exception as e:
            print(f"Error fill_email: {str(e)}")

    def fill_password(self):
        try:
            # Find the password input field by its 'id' attribute
            password_input = self.driver.find_element(By.ID, "password")
            print("Password input field found:", password_input)

            # Enter a password into the input field
            password_input.send_keys(PWD)

        except Exception as e:
            print(f"Error fill_password: {str(e)}")

    def click_signin(self):
        try:
            # Find the sign-in button by its 'aria-label' attribute and click it
            submit_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Sign in' and @type='submit']")
            print("Submit button found:", submit_button)
            
            # Click the sign-in button to submit the form
            submit_button.click()
            
            # Wait for a few seconds to observe the interaction
            time.sleep(5)

        except Exception as e:
            print(f"Error click_siginin: {str(e)}")

