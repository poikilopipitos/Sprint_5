from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators

def login(driver, email, password):

    wait = WebDriverWait(driver, 5)

    login_button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_ACCOUNT_BUTTON))
    login_button.click()
    wait.until(expected_conditions.visibility_of_element_located(locators.EMAIL_INPUT_TITLE))
    driver.find_element(*locators.EMAIL_INPUT_AUTORIZATION).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
    button = wait.until(expected_conditions.visibility_of_element_located(locators.LOGIN_BUTTON))
    button.click()

def test_switch_to_buns_section(driver, registered_user):
    email, password = registered_user
    login(driver, email, password)

    wait =  WebDriverWait(driver, 5)
    
    wait.until(expected_conditions.element_to_be_clickable(locators.SAUCES_TAB)).click()
    wait.until(expected_conditions.element_to_be_clickable(locators.BUNS_TAB)).click()
    
    wait.until(expected_conditions.visibility_of_element_located(locators.ACTIVE_BUNS_TAB))
    assert driver.find_element(*locators.ACTIVE_BUNS_TAB).is_displayed()


def test_switch_to_fillings_section(driver, registered_user):
    email, password = registered_user
    login(driver, email, password)
    
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.FILLINGS_TAB)).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.ACTIVE_FILLINGS_TAB))
    assert driver.find_element(*locators.ACTIVE_FILLINGS_TAB).is_displayed()


def test_switch_to_sauces_section(driver, registered_user):
    email, password = registered_user
    login(driver, email, password)

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(locators.SAUCES_TAB)).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(locators.ACTIVE_SAUCES_TAB))
    assert driver.find_element(*locators.ACTIVE_SAUCES_TAB).is_displayed()  