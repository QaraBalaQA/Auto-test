import time
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Users import Users
import Conf


def test1_Add_users_button_click():
    test1 = Users(Conf.User_email, Conf.User_password, Conf.Search_FIO_text)
    test1.Users_roles_button_click()
    Users.Add_users_button_click()
    Users.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.Add_user_button_xpath)))
    assert (Users.driver.find_element_by_xpath(Conf.Add_user_button_xpath).is_displayed())


def test2_Create_user_without_objects_and_organizations():
    test2 = Users(Conf.User_email, Conf.User_password, Conf.Search_FIO_text)
    test2.Surname = "Имя номер " + datetime.datetime.today().strftime("%Y%m%d%H%M%S")
    test2.Name = "Фамилия номер " + datetime.datetime.today().strftime("%Y%m%d%H%M%S")
    test2.Patronymic = "Отчество номер " + datetime.datetime.today().strftime("%Y%m%d%H%M%S")
    test2.XIN = Users.XIN_generate()
    test2.Email = "user" + datetime.datetime.today().strftime("%Y%m%d%H%M%S") + "@mail.ru"
    test2.insert_data()
    Users.driver.execute_script("window.scrollTo(0, 1080)")
    Users.Save_button_click()
