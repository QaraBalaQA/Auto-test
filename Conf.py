Base_url = 'http://172.27.117.31/userManage/users'
User_email = "seidualyayan@gmail.com"
Incorrect_user_email = "XXXvms-admin@srgdev.kz"
User_password = "QWas!@12"
Incorrect_user_password = "XXXQWas!@12"
User_name_text_xpath = "//p[@class='MuiTypography-root MuiTypography-body1']"
User_email_xpath = "//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]"
User_password_xpath = "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]"
Enter_button_xpath = "//span[text()='Войти в систему']"
Incorrect_login_label = "//span[contains(@class,'MuiTypography-root MuiListItemText-primary')]"
Incorrect_password_label_xpath = "//span[text()='Логин или пароль введен неверно, пожалуйста, проверьте данные или обратитесь к администратору']"
Incorrect_format_login_label_xpath = "//p[contains(@class,'MuiFormHelperText-root MuiFormHelperText-contained')]"
Incorrect_format_password_label_xpath = "//p[text()='Обязательно для заполнения']"
Password_type_xpath = "//input[@type='password']"
Eye_button_xpath = "//button[contains(@class,'MuiButtonBase-root MuiIconButton-root')]"
Text_type_xpath = "//input[@value='1q2w3e']"

Recover_password_button_xpath = "//span[contains(@class,'MuiTypography-root form-item')]"
Recover_password_label1_xpath = "//h5[contains(@class,'MuiTypography-root title')]"
Recover_password_label2_xpath = "//p[contains(@class,'MuiTypography-root form-item')]"
Recover_password_Email_xpath = "//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]"
Send_link_for_recovery_button_xpath = "//span[@class='MuiButton-label']"
Back_to_exit_screen_button_xpath = "(//span[@class='MuiButton-label'])[2]"

Menu_icon_xpath = "(//button[contains(@class,'MuiButtonBase-root MuiIconButton-root')])[2]"
Exit_button_xpath = "//span[text()='Выйти']"

Users_Roles_button_xpath = "//span[text()='Пользователи, роли']"
Add_user_button_xpath = "//button[contains(@class,'MuiButtonBase-root MuiButton-root')]/following-sibling::button"

Search_button_xpath = "//button[@type='submit']"
ID_Column_xpath = "//h6[text()='ID']"
Id_of_the_first_record_xpath = "(//p[@class='MuiTypography-root MuiTypography-body1'])[2]"
Dropdown_with_roles_xpath = "//div[contains(@class,'MuiInputBase-root MuiOutlinedInput-root')]"

Empty_role_span_xpath = "//span[contains(@class,'MuiTypography-root MuiListItemText-primary')]"
test_role_span_xpath = "//span[text()='Для автотестов']"
test_role_span_check_xpath="//p[text()='Для автотестов']"

Check_all_checkbox_xpath = "//div[@class='flex items-center']/following-sibling::h6"
Check_first_checkbox_xpath = "//div[@class='flex justify-center']"

Selected_users_text_xpath = "//p[text()='Выбрано пользователей : ']"
Count_selected_users_xpath = "//p[@class='MuiTypography-root MuiTypography-body1']/following-sibling::p[1]"

BLOCK_button_xpath = "//div[text()='Заблокировать']"
DELETE_button_xpath = "//div[text()='УДАЛИТЬ']"
DROP_PASSWORD_button_xpath = "//div[text()='Сбросить пароль']"
CANCEL_button_xpath = "//div[text()='ОТМЕНА']"

Blocked_users_checkbox_xpath = "(//div[contains(@class,'flex items-center')]//label)[2]"
Search_field_xpath = "//input[@placeholder='Найти пользователя по ФИО, e-mail, ИИН, организации, БИН']"

Search_FIO_text = "Автотест Автотестов Питонович"
Search_EMAIL_text = "autotest@yahoo.com"
Search_XIN_text = "000215502585"
Search_ID_text = "249"
Search_ORG_text = "Для автотестов"

ORG_text_xpath = "//div[@id='root']/main[1]/div[4]/div[2]/div[3]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/th[6]"
ID_text_xpath = "//p[text()='249']"
FIO_text_xpath = "//p[text()='Автотест Автотестов Питонович']"
XIN_text_xpath = "//p[text()='000215502585']"
EMAIL_text_xpath = "//p[text()='autotest@yahoo.com']"

Create_user_label_xpath = "//h5[text()='Создать пользователя']"
Surname_field_xpath = "//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')]"
Name_field_xpath = "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[2]"
Patronymic_field_xpath = "(//input[contains(@class,'MuiInputBase-input MuiOutlinedInput-input')])[3]"
XIN_field_xpath = "//input[@type='number']"
Email_field_xpath = "//input[@placeholder='e-mail']"
Save_button_xpath = "//div[text()='Сохранить']"