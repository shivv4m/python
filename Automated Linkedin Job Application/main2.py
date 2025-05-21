import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os
from selenium.common.exceptions import NoSuchElementException
load_dotenv()

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
PHONE = os.environ["PHONE"]



def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_element(By.XPATH, "//button[span[text()='Discard']]")
    discard_button.click()

URL = "https://www.linkedin.com/jobs/search/?currentJobId=4216336436&geoId=102713980&keywords=Pythonintern&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the LinkedIn job search page
driver.get(URL)
time.sleep(3)
sign_in_button = driver.find_element(By.CSS_SELECTOR, '[data-modal="base-sign-in-modal"]')
sign_in_button.click()
time.sleep(3)
email_input = driver.find_element(By.ID, "base-sign-in-modal_session_key")
email_input.send_keys(EMAIL)
password_input = driver.find_element(By.ID, "base-sign-in-modal_session_password")
password_input.send_keys(PASSWORD, Keys.ENTER)
time.sleep(4)
# apply_button = driver.find_element(By.ID, "jobs-apply-button-id")
# apply_button.click()
# time.sleep(2)
# phone = driver.find_element(By.ID,value="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4216336436-9-phoneNumber-nationalNumber")
# phone.send_keys(PHONE, Keys.ENTER)
# submit =driver.find_element(By.XPATH, "//button[.//span[text()='Submit application']]")
# submit.click()

all_listings = driver.find_elements(By.XPATH, "//li[contains(@class, 'scaffold-layout__list-item')]")
for listing in all_listings:
    print("Opening Listing")
    listing.click()
    time.sleep(2)
    try:
        # Click Apply Button
        apply_button = driver.find_element(By.ID, "jobs-apply-button-id")
        apply_button.click()
        time.sleep(5)
        phone = driver.find_element(By.CSS_SELECTOR,value="input.artdeco-text-input--input[type='text'][id*='phoneNumber-nationalNumber']")
        phone.send_keys(PHONE, Keys.ENTER)
        submit =driver.find_element(By.XPATH, "//button[.//span[text()='Submit application']]")
        if submit.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit.click()
        time.sleep(2)
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        abort_application()
        print("No application button, skipped.")
        continue
time.sleep(5)
driver.quit()