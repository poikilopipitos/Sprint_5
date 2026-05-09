from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators

def test_logout_from_personal_account(driver, registered_user):
    email, password = registered_user
    wait =  WebDriverWait(driver, 5)

    login_button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_ACCOUNT_BUTTON))
    login_button.click()
    wait.until(expected_conditions.visibility_of_element_located(locators.EMAIL_INPUT_TITLE))
    driver.find_element(*locators.EMAIL_INPUT_AUTORIZATION).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
    button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON))
    button.click()


    wait.until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON)).click()
    wait.until(expected_conditions.visibility_of_element_located(locators.LOGOUT_BUTTON)).click()
    wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON))
    
    assert driver.find_element(*locators.LOGIN_BUTTON).is_displayed()