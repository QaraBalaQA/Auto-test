import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Users import Users
import Conf


def test1_Users_roles_button_click():
    test1 = Users(Conf.User_email, Conf.User_password, Conf.Search_FIO_text)
    test1.Users_roles_button_click()
    assert Users.driver.find_element_by_xpath(Conf.Add_user_button_xpath).is_displayed()


def test2_Users_Sort_by_ID():
    Id_of_the_first_record = Users.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.Id_of_the_first_record_xpath)))
    check_text = Id_of_the_first_record.text
    Users.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.ID_Column_xpath)))
    ID_Column = Users.driver.find_element_by_xpath(Conf.ID_Column_xpath)
    ID_Column.click()
    ID_Column.click()
    assert (check_text != Users.driver.find_element_by_xpath(Conf.Id_of_the_first_record_xpath).text)
    ID_Column.click()
    assert (check_text == Users.driver.find_element_by_xpath(Conf.Id_of_the_first_record_xpath).text)
    Users.driver.refresh()


def test3_roles_dropdown():
    Users.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.Dropdown_with_roles_xpath)))
    Dropdown_with_roles = Users.driver.find_element_by_xpath(Conf.Dropdown_with_roles_xpath)
    Dropdown_with_roles.click()

    Users.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.test_role_span_xpath)))
    test_role_span = Users.driver.find_element_by_xpath(Conf.test_role_span_xpath)
    check_text = Users.driver.find_element_by_xpath(Conf.test_role_span_xpath).text
    test_role_span.click()

    Users.Search_button_click()

    Users.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.test_role_span_check_xpath)))
    test_role_span_check = Users.driver.find_element_by_xpath(Conf.test_role_span_check_xpath)
    try:
        assert (check_text == test_role_span_check.text)
    finally:
        Dropdown_with_roles.click()
        Users.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.Empty_role_span_xpath)))
        Empty_role_span = Users.driver.find_element_by_xpath(Conf.Empty_role_span_xpath)
        Empty_role_span.click()
        Users.Search_button_click()


def test4_select_all_checkbox():
    Users.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.Check_all_checkbox_xpath)))
    Check_all_checkbox = Users.driver.find_element_by_xpath(Conf.Check_all_checkbox_xpath)
    Check_all_checkbox.click()
    time.sleep(1)

    try:
        assert Users.driver.find_element_by_xpath(Conf.Selected_users_text_xpath)
        assert Users.driver.find_element_by_xpath(Conf.Count_selected_users_xpath).text == "50"
        assert Users.driver.find_element_by_xpath(Conf.BLOCK_button_xpath)
        assert Users.driver.find_element_by_xpath(Conf.DELETE_button_xpath)
        assert Users.driver.find_element_by_xpath(Conf.DROP_PASSWORD_button_xpath)
        assert Users.driver.find_element_by_xpath(Conf.CANCEL_button_xpath)

    finally:
        Check_all_checkbox.click()
        time.sleep(1)


def test5_blocked_users_list():
    Users.Blocked_checkbox_click()
    Users.Search_button_click()
    time.sleep(2)

    Check_first_checkbox = Users.driver.find_element_by_xpath(Conf.Check_first_checkbox_xpath)
    Check_first_checkbox.click()

    try:
        assert (not Check_first_checkbox.is_selected())
    finally:
        Users.driver.refresh()
        Users.Search_button_click()
        time.sleep(1)


def test6_search_by_FIO():
    test6 = Users(Conf.User_email, Conf.User_password, Conf.Search_FIO_text)
    test6.Search()
    try:
        assert (Users.driver.find_element_by_xpath(Conf.FIO_text_xpath).text == Conf.Search_FIO_text)
    finally:
        Users.driver.refresh()
        Users.Search_button_click()
        time.sleep(1)


def test7_search_by_EMAIL():
    test7 = Users(Conf.User_email, Conf.User_password, Conf.Search_EMAIL_text)
    test7.Search()
    try:
        assert (Users.driver.find_element_by_xpath(Conf.EMAIL_text_xpath).text == Conf.Search_EMAIL_text)
    finally:
        Users.driver.refresh()
        Users.Search_button_click()
        time.sleep(1)


def test8_search_by_XIN():
    test8 = Users(Conf.User_email, Conf.User_password, Conf.Search_XIN_text)
    test8.Search()
    try:
        assert (Users.driver.find_element_by_xpath(Conf.XIN_text_xpath).text == Conf.Search_XIN_text)
    finally:
        Users.driver.refresh()
        Users.Search_button_click()
        time.sleep(1)


def test8_search_by_ORG():
    test8 = Users(Conf.User_email, Conf.User_password, Conf.Search_ORG_text)
    test8.Search()
    try:
        assert (Users.driver.find_element_by_xpath(Conf.ORG_text_xpath).text == Conf.Search_ORG_text)
    finally:
        Users.driver.refresh()
        Users.Search_button_click()
        time.sleep(1)
