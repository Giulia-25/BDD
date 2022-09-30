from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    #locators
    USERNAME_FIELD =(By.ID, 'username')
    PASSWORD_FIELD =(By.ID, 'password')
    LOGIN_BUTTON = (By.CLASS_NAME, 'radius')
    FLASH_TEXT = (By.ID, 'flash')

    # URL
    URL = 'https://the-internet.herokuapp.com/login'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def insert_username_field(self, username):
        self.browser.find_element(self.USERNAME_FIELD).send_keys(username)

    def insert_password_field(self, password):
        self.browser.find_element(self.PASSWORD_FIELD).send_keys(password)

    def click_login_button(self):
        self.browser.find_element(self.LOGIN_BUTTON).click()

    def get_flash_message(self):
        return self.browser.find_element(self.FLASH_TEXT).text

    def login(self, username, password):
        self.load_page()
        self.insert_username_field(username)
        self.insert_password_field(password)
        self.click_login_button()


    def get_current_url(self):
       return self.browser.current_url

    def wait_for_login_button(self):
        wait = WebDriverWait(self.browser, 5)
        wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))