from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import InvalidSelectorException as EX


"""this class is parent of all page classes 
it contains all common action methods and utilities for all pages"""

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].click();", element)
        except EX as e:
            print("Exception! Can't Click on element")

    def input_element(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        except EX as e:
            print("Exception! Can't Click on element")

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def get_title(self):
        return self.driver.title

    def get_element_attribute(self, by_locator, attribute_name):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(attribute_name)

    def verify_element_displayed(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
            return element.is_displayed()
        except:
            return False
