import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class JobsPage:
    def __init__(self, driver):
        self.driver = driver

    def apply_store(self):
        try:
            self.scroll()
            self.get_all_jobs()

        except Exception as e:
            print(f"Error apply_store: {str(e)}")

    def scroll(self):
        try:
            child_div = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results-list"))
            )
            
            # Scroll the specific div element
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", child_div)
            is_scrollable = self.driver.execute_script('return arguments[0].scrollHeight > arguments[0].clientHeight;', child_div)
            
            if is_scrollable:
                print("The element is scrollable child_div")
            else:
                print("The element is not scrollable child_div")

        except Exception as e:
            print(f"Error scroll: {str(e)}")

    def get_all_jobs(self):
        try:
            for i in range(1, 5):
                x = f"(//ul[contains(@class, 'scaffold-layout__list-container')]//li[{i}]//div[contains(@class, 'job-card-container--clickable')])[1]"
                job_element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, x))
                )
                
                # Click on the job element
                job_element.click()
                time.sleep(5)
                self.apply_save()
        except Exception as e:
            print(f"Error get_all_jobs: {str(e)}")

    def apply_save(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//button[contains(@class, 'jobs-apply-button')])[1]"))
            )
    
            # Get the text inside the <span> element
            span_text = button.find_element(By.XPATH, "./span").text.strip().lower()
            
            # Check if the text is 'easy apply'
            print("span_text",span_text)
            if span_text == "easy apply":
                # Click the button
                self.easyapply_job()
            else:
                self.save_job()
                pass
            
        except Exception as e:
            print(f"Error apply_save: {str(e)}")

    def easyapply_job(self):
        currentbutton="next"
        

        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Continue to next step']"))

            )
            print("here",button)
            button.click()
            print("here clicked",button)


            while currentbutton!="submit":
                print("currentbutton",currentbutton)
                form = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "form")))
                # Find the h3 element within the form
                h3_element = form.find_element(By.TAG_NAME, "h3")
                section_text = h3_element.text.strip().lower()
                if "contact info" in section_text:
            # Click on the Next button for personal section
                    next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Continue to next step']"))

            )
                    time(2)
                    print(next_button,"contact info",section_text)

                    next_button.click()
                    time(2)

                elif "resume" in section_text:
                    # Click on the Next button for resume section
                    next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Continue to next step']"))
            )
                    time(2)
                    next_button.click()
                    time(2)

                elif "work authorization" in section_text:
                    # Click on the Review button for work auth section
                    review_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Review your application']"))
            )
                    review_button.click()
                    
                elif "review your application" in section_text:
                    # Click on the Submit button for submit section
                    submit_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Submit application']"))
            )
                    submit_button.click()
                    currentbutton="submit"
                    break
                    # Exit the script or further action
                elif "additional questions" in section_text:
                    time(2)

                    # Fill out the form and click Next for the add section
                    # Assuming you have fields to fill and then proceed
                    form = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "form")))
                    input_fields = form.find_elements(By.TAG_NAME, "input")
                    for field in input_fields:
                        print(field.get_attribute("required"),"field.get_attribute('required')")
                        if "required" in field.get_attribute("required"):
                            # Enter "2" into the required input field
                            field.send_keys("2")
                    time(2)

                    next_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Continue to next step']"))
            )

                    next_button.click()
                    time(2)

                else:
                    print("Section not recognized")

            

        except Exception as e:
            print(f"Error easyapply_job: {str(e)}")

    def save_job(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//button[contains(@class, 'jobs-save-button')])[1]"))
            )
            button.click()
            
        except Exception as e:
            print(f"Error save_job: {str(e)}")

