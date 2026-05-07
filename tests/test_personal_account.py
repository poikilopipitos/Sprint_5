from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators

def test_logout_from_personal_account(driver):

    wait =  WebDriverWait(driver, 5)

    login_button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_ACCOUNT_BUTTON))
    login_button.click()
    wait.until(expected_conditions.visibility_of_element_located(locators.EMAIL_INPUT_TITLE))
    driver.find_element(*locators.EMAIL_INPUT_AUTORISATION).send_keys("ekaterinaaboimova45777@yandex.ru")
    driver.find_element(*locators.PASSWORD_INPUT).send_keys("123456")
    button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON))
    button.click()


    wait.until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON)).click()
    wait.until(expected_conditions.visibility_of_element_located(locators.LOGOUT_BUTTON)).click()
    wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON))
    
    assert driver.find_element(*locators.LOGIN_BUTTON).is_displayed()