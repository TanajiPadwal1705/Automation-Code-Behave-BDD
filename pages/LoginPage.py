from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    TXT_USERNAME = (By.NAME, "user-name")
    TXT_PASSWORD = (By.NAME, "password")
    BTN_LOGIN = (By.ID, "login-button")
    MSG_INVALIDCREDS = (By.CLASS_NAME, "error-button")

    """Constructor of CarrersPage class"""

    def __init__(self, driver):
        super().__init__(driver)

    def enter_login_credentials(self, user, pwd):
        self.input_element(self.TXT_USERNAME, user)
        self.input_element(self.TXT_PASSWORD, pwd)

    # def enter_username(self, user):
    #     self.input_element(self.TXT_USERNAME, user)
    #
    # def enter_password(self, pwd):
    #     self.input_element(self.TXT_PASSWORD, pwd)

    def enter_login(self):
        self.click_element(self.BTN_LOGIN)

    def validateTitle(self):
        print(self.get_title())
        assert self.get_title() == "Swag Labs"

    def validateInvalidCredentials(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS) == 'Invalid Credentials'

    def validateEmptyUsername(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS) == "UserName cannot be empty"

    def validateEmptyPassword(self):
        assert self.get_element_text(self.MSG_INVALIDCREDS) == "Password cannot be empty"

