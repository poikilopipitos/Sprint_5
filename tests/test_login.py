from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators

class TestLogin:
    def login(self,driver, email, password):

        wait = WebDriverWait(driver, 5)

        wait.until(expected_conditions.visibility_of_element_located(locators.EMAIL_INPUT_TITLE))
        driver.find_element(*locators.EMAIL_INPUT_AUTORIZATION).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)


    def test_login_via_main_page_login_button(self,driver, user_data):
        email, password = user_data
        wait = WebDriverWait(driver, 5)

        login_button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_ACCOUNT_BUTTON))
        login_button.click()

        self.login(driver, email, password)

        button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON))
        button.click()

        wait.until(expected_conditions.visibility_of_element_located(locators.PLACE_ORDER_BUTTON))

        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()

        logout_button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGOUT_BUTTON))
        assert logout_button.is_displayed()


    def test_login_via_password_recovery_form(self,driver, user_data):
        email, password = user_data
        wait = WebDriverWait(driver, 5)

        driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()

        wait.until(expected_conditions.visibility_of_element_located(locators.FORGOT_PASSWORD_LINK)).click()
        wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_LINK)).click()

        self.login(driver, email, password)
    
        button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON))
        button.click()

        wait.until(expected_conditions.visibility_of_element_located(locators.PLACE_ORDER_BUTTON))
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()
    
        logout_button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGOUT_BUTTON))
        assert logout_button.is_displayed()


    def test_login_via_personal_account_button(self,driver, user_data):
        email, password = user_data
        wait = WebDriverWait(driver, 5)

        wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_ACCOUNT_BUTTON)).click()

        self.login(driver, email, password)

        button = wait.until(expected_conditions.element_to_be_clickable(locators.LOGIN_BUTTON))
        button.click()

        wait.until(expected_conditions.visibility_of_element_located(locators.PLACE_ORDER_BUTTON))

        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()

        logout_button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGOUT_BUTTON))
        assert logout_button.is_displayed()


    def test_login_via_registration_form_link(self,driver, user_data):
        email, password = user_data
        wait = WebDriverWait(driver, 5)

        driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.REGISTER_LINK).click()
    
        wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_LINK)).click()

        self.login(driver, email, password)
    
        button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON))
        button.click()

        wait.until(expected_conditions.visibility_of_element_located(locators.PLACE_ORDER_BUTTON))
        driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()

        logout_button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGOUT_BUTTON))
        assert logout_button.is_displayed()