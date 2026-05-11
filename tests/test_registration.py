from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators


class TestRegistration:
    def test_successful_registration_with_valid_data(self, driver,name,email,password):

        wait =  WebDriverWait(driver, 5)

        driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.REGISTER_LINK).click()
    
        wait.until(expected_conditions.visibility_of_element_located(locators.REGISTER_BUTTON))

        driver.find_element(*locators.NAME_INPUT).send_keys(name)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REGISTER_BUTTON).click()

        wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_TITLE))
        assert driver.find_element(*locators.LOGIN_TITLE).is_displayed()


    def test_registration_fails_with_short_password(self, driver,name,email):

        wait =  WebDriverWait(driver, 5)

        driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.REGISTER_LINK).click()
        wait.until(expected_conditions.visibility_of_element_located(locators.REGISTER_BUTTON))

        driver.find_element(*locators.NAME_INPUT).send_keys(name)
        driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys("12345")
        wait.until(expected_conditions.visibility_of_element_located(locators.REGISTER_BUTTON)).click()

        error = driver.find_element(*locators.INVALID_PASSWORD_ERROR)
        assert error.is_displayed()


    def test_registration_fails_with_empty_name(self, driver,email,password):

        wait =  WebDriverWait(driver, 5)

        driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.REGISTER_LINK).click()
        wait.until(expected_conditions.visibility_of_element_located(locators.REGISTER_BUTTON))

        driver.find_element(*locators.NAME_INPUT).send_keys('')
        driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REGISTER_BUTTON).click()

        assert not driver.find_elements(*locators.LOGIN_TITLE)

    
    def test_registration_fails_with_invalid_email_format(self, driver,name,password):

        wait =  WebDriverWait(driver, 5)

        driver.find_element(*locators.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(*locators.REGISTER_LINK).click()
        wait.until(expected_conditions.visibility_of_element_located(locators.REGISTER_BUTTON))

        driver.find_element(*locators.NAME_INPUT).send_keys(name)
        driver.find_element(*locators.EMAIL_INPUT).send_keys("qwerty")
        driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*locators.REGISTER_BUTTON).click()

        assert not driver.find_elements(*locators.LOGIN_TITLE)





