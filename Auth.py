import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import Conf


class Auth:
    CheckTrecker = True
    EXE_PATH = r'C:\Users\User\Desktop\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=EXE_PATH)
    options = driver.create_options()
    options.add_argument("no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=800,600")
    options.add_argument("--disable-dev-shm-usage")
    options.set_headless()

    def __init__(self, Email, Password):
        self.Email = Email
        self.Password = Password

    def Menu_button_click():
        Menu_button = Auth.driver.find_element_by_xpath(Conf.Menu_icon_xpath)
        Menu_button.click()

    def Exit_button_click():
        Exit_button = Auth.driver.find_element_by_xpath(Conf.Exit_button_xpath)
        Exit_button.click()

    def Correct_login_and_password(self):
        driver = Auth.driver
        driver.get(Conf.Base_url)
        driver.maximize_window()
        Auth.Enter_Login_Password(self)

    def Enter_Login_Password(self):
        Auth.CheckTrecker = True

        try:
            Email_field = Auth.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.User_email_xpath)))
            Email_field.send_keys(self.Email)

            Password_field = Auth.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.User_password_xpath)))
            Password_field.send_keys(self.Password)

            Enter_Button = Auth.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.Enter_button_xpath)))
            Enter_Button.click()

            time.sleep(0.4)

        except NoSuchElementException:
            Auth.CheckTrecker = False
            pass

    def Eye_button(self):
        Auth.CheckTrecker = True
        Password_field = Auth.driver.find_element_by_xpath(Conf.User_password_xpath)
        Password_field.send_keys(self.Password)
        time.sleep(0.2)

    def Recovery_button(self):
        Auth.CheckTrecker = True
        Recovery_button = Auth.driver.find_element_by_xpath(Conf.Recover_password_button_xpath)
        Recovery_button.click()
