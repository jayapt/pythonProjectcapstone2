from Data import data
from Locators import locators
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Menu:
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

    def menu_validation(self):

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, locators.WebLocators().admin_locator))).click()

        menu_options = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance", "Dashboard",
                        "Directory", "Maintenance", "Claim", "Buzz"]

        for option in menu_options:
            locator = f"//li/a/span[text()='{option}']"
            try:
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, locator)))
                print(f"{option} is displayed.")
            except:
                print(f"{option} is NOT displayed.")



if __name__ == '__main__':
    menu_list = Menu()
    if menu_list.booting_function() and menu_list.login():
        menu_list.menu_validation()
        menu_list.quit()
