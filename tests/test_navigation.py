from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_navigate_from_profile_to_constructor_via_constructor_button(driver,login):

    wait =  WebDriverWait(driver, 5)

    wait.until(expected_conditions.element_to_be_clickable((By.XPATH ,"//p[text()='Личный Кабинет']"))).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Выход']")))

    wait.until(expected_conditions.element_to_be_clickable((By.XPATH ,"//p[text()='Конструктор']"))).click()

    offer = wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Оформить заказ']")))
    assert offer.is_displayed()


def test_navigate_from_profile_to_constructor_via_logo(driver,login):

    wait =  WebDriverWait(driver, 5)

    wait.until(expected_conditions.element_to_be_clickable((By.XPATH ,"//p[text()='Личный Кабинет']"))).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Выход']")))

    wait.until(expected_conditions.visibility_of_element_located((By.CLASS_NAME ,'AppHeader_header__logo__2D0X2'))).click()
    
    offer = wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Оформить заказ']")))
    assert offer.is_displayed()


def test_navigate_to_personal_account(driver,login):

    wait =  WebDriverWait(driver, 5)

    wait.until(expected_conditions.element_to_be_clickable((By.XPATH ,"//p[text()='Личный Кабинет']")))
    driver.find_element(By.XPATH , "//p[text()='Личный Кабинет']").click()

    logout_button = wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Выход']")))
    assert logout_button.is_displayed()