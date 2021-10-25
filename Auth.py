from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Conf


class Auth:
    CheckTrecker = True
    Gcode = ""
    EXE_PATH = r'C:\Users\User\Desktop\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=EXE_PATH)
    wait = WebDriverWait(driver, 5)

    def __init__(self, Email, Password):
        self.Email = Email
        self.Password = Password

    def Citadel_auth(self):
        driver = Auth.driver
        driver.maximize_window()
        driver.get(Conf.Citadel_base_url)

        Citadel_email_field = Auth.wait.until(EC.element_to_be_clickable(By.XPATH, Conf.Citadel_email_field_xpath))
        Citadel_email_field.send_keys(self.Email)
        Citadel_sign_in_button = driver.find_element_by_xpath(Conf.Citadel_sign_in_button_xpath)
        Citadel_sign_in_button.click()

        # Вызываем метод для получения кода из письма
        Auth.Gmail_code(self)

        # Переходим на страницу верификации и вводим полученный код
        Auth.driver.get(Conf.Citadel_verification_page)
        Citadel_verification_code_field = Auth.wait.until(EC.element_to_be_clickable(By.XPATH, Conf.Citadel_verification_code_field_xpath))
        Citadel_verification_code_field.send_keys(Auth.Gcode)
        Citadel_verification_code_confirm_button = driver.find_element_by_xpath(Conf.Citadel_verification_code_confirm_button_xpath)
        Citadel_verification_code_confirm_button.click()

        # Проверка по url
        if (Conf.Citadel_main_page_url != driver.current_url):
            Auth.CheckTrecker = False

    def Gmail_code(self):
        Auth.driver.get(Conf.Gmail_base_url)
        Gmail_sign_button = Auth.wait.until(EC.element_to_be_clickable(By.XPATH, Conf.Gmail_sign_button_xpath))
        Gmail_sign_button.click()

        #Заполняем поле Email
        Gmail_email_field = Auth.wait.until(EC.element_to_be_clickable(By.XPATH, Conf.Gmail_email_field_xpath))
        Gmail_email_field.send_keys(self.Email)
        Gmail_next_button = Auth.driver.find_element_by_xpath(Conf.Gmail_next_button_xpath)
        Gmail_next_button.click()
        #Заполняем поле Password
        Gmail_password_field = Auth.wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, Conf.Gmail_password_field_css_selector))
        Gmail_password_field.send_keys(self.Password)
        Gmail_next_button.click()
        # Открываем сообщение с верификационным кодом и вытягиваем его от туда в гобальную переменную
        Gmail_Citadel_msg = Auth.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.Gmail_Citadel_msg_xpath)))
        Gmail_Citadel_msg.click()
        Gmail_Citadel_code = Auth.wait.until(EC.element_to_be_clickable((By.XPATH, Conf.Gmail_Citadel_code_xpath)))
        Auth.Gcode = Gmail_Citadel_code.text
