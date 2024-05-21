from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import BASE_URL 
from config import ROLES 

from pages.AuthPage import AuthPage
import time

from pages.JobsPage import JobsPage
from pages.LandingPage import LandingPage

# Set up the WebDriver service
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
roles=ROLES

try:
    # Open the LinkedIn job page
    driver.get(BASE_URL)
    
    
    # Authenticate user from config
    auth_page = AuthPage(driver)
    auth_page.authenticate()
    time.sleep(20)
    landing_page = LandingPage(driver)
    jobs_page = JobsPage(driver)

    for role in roles:
        landing_page.search_job(role)
        jobs_page.apply_store()
        # for i in range(10):
        #     jobs_page.apply_store()

    time.sleep(2)
    

finally:
    # Quit the WebDriver session
    driver.quit()


