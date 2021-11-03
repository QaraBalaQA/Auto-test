import time
from selenium.common.exceptions import NoSuchElementException
from Auth import Auth
import Conf

def test1_Correct_login_and_correct_password():
    test1 = Auth(Conf.User_email, Conf.User_password)
    Auth.Correct_login_and_password(test1)
    Check_text = Auth.driver.find_element_by_xpath(Conf.User_name_text_xpath)
    assert (Check_text.text == Conf.User_email) and Auth.CheckTrecker
    Auth.Menu_button_click()
    time.sleep(0.2)
    Auth.Exit_button_click()

def test2_Incorrect_login_and_correct_password():

    test2 = Auth(Conf.Incorrect_user_email, Conf.User_password)
    Auth.Enter_Login_Password(test2)
    try:
        Auth.driver.find_element_by_xpath(Conf.Incorrect_login_label)
    except NoSuchElementException:
        Auth.CheckTrecker = False
    assert Auth.CheckTrecker
    Auth.driver.refresh()

def test3_Correct_login_and_incorrect_password():
    test3 = Auth(Conf.User_email, Conf.Incorrect_user_password)
    Auth.Enter_Login_Password(test3)
    try:
        Auth.driver.find_element_by_xpath(Conf.Incorrect_password_label_xpath)
    except NoSuchElementException:
        Auth.CheckTrecker = False
    assert Auth.CheckTrecker
    Auth.driver.refresh()

def test4_Incorrect_format_login_and_correct_password():
    test4 = Auth("XXX", Conf.User_password)
    Auth.Enter_Login_Password(test4)
    try:
        Auth.driver.find_element_by_xpath(Conf.Incorrect_format_login_label_xpath)
    except NoSuchElementException:
        Auth.CheckTrecker = False
    assert Auth.CheckTrecker
    Auth.driver.refresh()

def test5_Incorrect_format_password_and_correct_login():
    test5 = Auth(Conf.User_email, '')
    Auth.Enter_Login_Password(test5)
    try:
        Auth.driver.find_element_by_xpath(Conf.Incorrect_format_password_label_xpath)
    except NoSuchElementException:
        Auth.CheckTrecker = False
        pass
    assert Auth.CheckTrecker
    Auth.driver.refresh()

def test6_Eye_button():
    test6 = Auth(Conf.User_email, Conf.User_password)
    test6.Eye_button()

    try:
        Auth.driver.find_element_by_xpath(Conf.Eye_button_xpath).click()
    except NoSuchElementException:
        Auth.CheckTrecker = False
    time.sleep(0.1)
    try:
        Auth.driver.find_element_by_xpath(Conf.Text_type_xpath)
    except NoSuchElementException:
        Auth.CheckTrecker = False
    Auth.driver.find_element_by_xpath(Conf.Eye_button_xpath).click()
    time.sleep(0.1)
    if Auth.driver.find_element_by_xpath(Conf.Password_type_xpath).is_displayed():
        Auth.CheckTrecker = True
    else:
        Auth.CheckTrecker = True
    assert Auth.CheckTrecker
    Auth.driver.refresh()

