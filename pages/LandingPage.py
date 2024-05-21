from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from config import USER_NAME 
from config import PWD 


class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    def search_job(self,role):
        try:
            self.enter_role(role)
            self.click_jobs_tab()
    
        except Exception as e:
            print(f"Error search_job: {str(e)}")

    def click_jobs_tab(self):
        try:
            sign_in_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@id='search-reusables__filters-bar']/ul/li[1]/button"))
            )
            sign_in_button.click()
    
        except Exception as e:
            print(f"Error click_jobs_tab: {str(e)}")

    def enter_role(self,role):
        try:
            # Find the username input field by its 'id' attribute
            search_box = self.driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
            print("search_box input field found:", search_box)
            
            # Enter a username into the input field
            search_box.send_keys(role)
            # Simulate pressing the Enter key
            search_box.send_keys(Keys.ENTER)

            time.sleep(2)

        except Exception as e:
            print(f"Error enter_role: {str(e)}")



