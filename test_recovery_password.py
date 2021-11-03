from selenium.common.exceptions import NoSuchElementException
from Auth import Auth
import Conf

def test1_Recovery_button_click():
    test7 = Auth(Conf.User_email, Conf.User_password)
    test7.Recovery_button()
    try:
        Auth.driver.find_element_by_xpath(Conf.Recover_password_label1_xpath)
        Auth.driver.find_element_by_xpath(Conf.Recover_password_label2_xpath)
        Auth.driver.find_element_by_xpath(Conf.Recover_password_Email_xpath)
        Auth.driver.find_element_by_xpath(Conf.Send_link_for_recovery_button_xpath)
        Auth.driver.find_element_by_xpath(Conf.Back_to_exit_screen_button_xpath)
    except NoSuchElementException:
        Auth.CheckTrecker = False
    assert Auth.CheckTrecker