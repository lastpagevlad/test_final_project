from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    # LOGIN_EDIT_FORM = (By.CSS_SELECTOR, "#id_login-username")
    # PASSWORD_EDIT_FORM = (By.CSS_SELECTOR, "#id_login-password")
    # REGISTRATION_EDIT_FORM_MAIL = (By.CSS_SELECTOR,"#id_registration-email")
    # REGISTRATION_EDIT_FORM_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    # REGISTRATION_EDIT_FORM_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    # LOGIN_BUTTON = (By.NAME,"login_submit")
    # REGISTRATION_BUTTON = (By.NAME, "registration_submit")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")