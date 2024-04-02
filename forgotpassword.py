# # Import necessary modules and classes
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data import data
from Locators import locators

class PasswordResetValidation:
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    def booting_function(self):
        try:
            self.driver.maximize_window()
            self.driver.get(data.WebData().url)
            return True
        except Exception as e:
            print(f"ERROR: Unable to start the browser: {e}")
            return False

    def quit(self):
        self.driver.quit()

    def forgot_password(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
                data.WebData().username)

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().forgot_password))).click()

            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().resetpassword_username))).send_keys(
                data.WebData().reset_username)
            print("Entering username: ", data.WebData().reset_username)

            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, locators.WebLocators().reset_button))).click()
            print("Password reset initiated successfully.")

        except Exception as e:
            print(f"Error during password reset: {e}")



if __name__ == "__main__":
    password_reset_validator = PasswordResetValidation()

    if password_reset_validator.booting_function():
        password_reset_validator.forgot_password()
        password_reset_validator.quit()