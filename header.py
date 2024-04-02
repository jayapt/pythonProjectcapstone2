from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Data import data
from Locators import locators


class Header_validation:
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

    def login(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.NAME, locators.WebLocators().username_locator))).send_keys(
                data.WebData().username)

            self.driver.find_element(by=By.NAME, value=locators.WebLocators().password_locator).send_keys(
                data.WebData().password)

            self.driver.find_element(by=By.XPATH, value=locators.WebLocators().login_button_locator).click()
            print("Login successful.")
            return True
        except Exception as e:
            print(f"Error during login: {e}")
            return False

    def header_validation(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin_locator))).click()

        header_options = ["User Management", "Job", "Organisation", "Qualification", "Nationalities",
                          "Corporate Branding", "Configuration"]

        for index, option in enumerate(header_options, start=1):
            locator = f"//header/div[2]/nav/ul/li[{index}]"
            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, locator)))
                print(f"{option} is displayed.")
            except:
                print(f"{option} is NOT displayed.")



if __name__ == '__main__':
    header_list = Header_validation()
    if header_list.booting_function() and header_list.login():
        header_list.header_validation()
        header_list.quit()

