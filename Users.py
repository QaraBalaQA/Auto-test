import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Auth import Auth
import Conf


class Users(Auth):
    def __init__(self, Email, Password, Stext):
        self.Email = Email
        self.Password = Password
        self.Stext = Stext

    def Users_roles_button_click(self):
        Users.Correct_login_and_password(self)
        Users_roles_button = Users.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.Users_Roles_button_xpath)))
        Users_roles_button.click()

    def Search_button_click():
        Search_button = Users.driver.find_element_by_xpath(Conf.Search_button_xpath)
        Search_button.click()
        time.sleep(1)

    def Check_all_checkbox():
        Users.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.Check_all_checkbox_xpath)))
        Check_all_checkbox = Users.driver.find_element_by_xpath(Conf.Check_all_checkbox_xpath)
        Check_all_checkbox.click()

    def Search(self):
        Users.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.Search_field_xpath)))
        Search_field = Users.driver.find_element_by_xpath(Conf.Search_field_xpath)
        Search_field.send_keys(self.Stext)
        Users.Search_button_click()
        time.sleep(1)

    def Search_clear():
        Search_field = Users.driver.find_element_by_xpath(Conf.Search_field_xpath)
        Search_field.clear()

    def Blocked_checkbox_click():
        Blocked_users_checkbox = Users.driver.find_element_by_xpath(Conf.Blocked_users_checkbox_xpath)
        Blocked_users_checkbox.click()

    def Add_users_button_click():
        Add_users_button = Users.driver.find_element_by_xpath(Conf.Add_user_button_xpath)
        Add_users_button.click()

    def insert_data(self):
        Surname_field = Users.driver.find_element_by_xpath(Conf.Surname_field_xpath)
        Surname_field.send_keys(self.Surname)

        Name_field = Users.driver.find_element_by_xpath(Conf.Name_field_xpath)
        Name_field.send_keys(self.Name)

        Patronymic_field = Users.driver.find_element_by_xpath(Conf.Patronymic_field_xpath)
        Patronymic_field.send_keys(self.Patronymic)

        XIN_field = Users.driver.find_element_by_xpath(Conf.XIN_field_xpath)
        XIN_field.send_keys(self.XIN)

        Email_field = Users.driver.find_element_by_xpath(Conf.Email_field_xpath)
        Email_field.send_keys(self.Email)

    def Save_button_click():
        Save_button = Users.driver.find_element_by_xpath(Conf.Save_button_xpath)
        Save_button.click()

    def XIN_generate():
        # год
        x1 = random.randrange(1, 9)
        x2 = random.randrange(1, 9)

        # месяц
        x3 = random.randrange(0, 1)

        if (x3 == 1):
            x4 = random.randrange(0, 2)
        else:
            x4 = random.randrange(1, 9)

        # день
        x5 = random.randrange(0, 3)

        if (x5 == 0):
            x6 = random.randrange(0, 9)
        if (x5 == 1):
            x6 = random.randint(0, 9)
        if (x5 == 2):
            x6 = random.randint(0, 8)
        if (x5 == 3):
            x6 = random.randrange(0, 1)

        x7 = random.randrange(1, 6)
        x8 = random.randrange(0, 9)
        x9 = random.randrange(0, 9)
        x10 = random.randrange(0, 9)
        x11 = random.randrange(0, 9)
        x12 = random.randrange(0, 9)
        XIN = str(x1) + str(x2) + str(x3) + str(x4) + str(5) + str(x6) + str(x7) + str(x8) + str(x9) + str(x10) + str(x11) + str(x12)
        return XIN