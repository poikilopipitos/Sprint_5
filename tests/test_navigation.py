from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators

def login(driver):

    wait = WebDriverWait(driver, 5)

    login_button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_ACCOUNT_BUTTON))
    login_button.click()
    wait.until(expected_conditions.visibility_of_element_located(locators.EMAIL_INPUT_TITLE))
    driver.find_element(*locators.EMAIL_INPUT_AUTORISATION).send_keys("ekaterinaaboimova45777@yandex.ru")
    driver.find_element(*locators.PASSWORD_INPUT).send_keys("123456")
    button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON))
    button.click()


def test_navigate_from_profile_to_constructor_via_constructor_button(driver):

    wait =  WebDriverWait(driver, 5)

    login(driver)

    wait.until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON)).click()
    wait.until(expected_conditions.visibility_of_element_located(locators.LOGOUT_BUTTON))

    wait.until(expected_conditions.element_to_be_clickable(locators.CONSTRUCTOR_LINK)).click()

    offer = wait.until(expected_conditions.visibility_of_element_located(locators.PLACE_ORDER_BUTTON))
    assert offer.is_displayed()


def test_navigate_from_profile_to_constructor_via_logo(driver):

    wait =  WebDriverWait(driver, 5)

    login(driver)

    wait.until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON)).click()
    wait.until(expected_conditions.visibility_of_element_located(locators.LOGOUT_BUTTON))

    wait.until(expected_conditions.visibility_of_element_located(locators.HEADER_LOGO)).click()
    
    offer = wait.until(expected_conditions.visibility_of_element_located(locators.PLACE_ORDER_BUTTON))
    assert offer.is_displayed()


def test_navigate_to_personal_account(driver):

    wait =  WebDriverWait(driver, 5)

    login(driver)

    wait.until(expected_conditions.element_to_be_clickable(locators.PERSONAL_ACCOUNT_BUTTON))
    driver.find_element(*locators.PERSONAL_ACCOUNT_BUTTON).click()

    logout_button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGOUT_BUTTON))
    assert logout_button.is_displayed()