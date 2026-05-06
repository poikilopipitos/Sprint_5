from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_via_main_page_login_button(driver):

    wait = WebDriverWait(driver, 5)

    login_button = wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Войти в аккаунт']")))
    login_button.click()

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//label[text()='Email']")))
    driver.find_element(By.XPATH , "//label[text()='Email']/following-sibling::input").send_keys("ekaterinaaboimova45777@yandex.ru")
    driver.find_element(By.XPATH , "//label[text()='Пароль']/following-sibling::input").send_keys("123456")

    button = wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Войти']")))
    button.click()

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Оформить заказ']")))

    driver.find_element(By.XPATH , "//p[text()='Личный Кабинет']").click()

    logout_button = wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Выход']")))
    assert logout_button.is_displayed()


def test_login_via_password_recovery_form(driver):

    wait = WebDriverWait(driver, 5)

    driver.find_element(By.XPATH , "//button[text()='Войти в аккаунт']").click()

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH , "//a[@href='/forgot-password']"))).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH , "//a[@href='/login']"))).click()

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//label[text()='Email']")))
    driver.find_element(By.XPATH , "//label[text()='Email']/following-sibling::input").send_keys("ekaterinaaboimova45777@yandex.ru")
    driver.find_element(By.XPATH , "//label[text()='Пароль']/following-sibling::input").send_keys("123456")
    
    button = wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Войти']")))
    button.click()

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH , "//p[text()='Личный Кабинет']").click()
    
    logout_button = wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Выход']")))
    assert logout_button.is_displayed()


def test_login_via_personal_account_button(driver):

    wait = WebDriverWait(driver, 5)

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Войти в аккаунт']"))).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//label[text()='Email']")))
    driver.find_element(By.XPATH , "//label[text()='Email']/following-sibling::input").send_keys("ekaterinaaboimova45777@yandex.ru")
    driver.find_element(By.XPATH , "//label[text()='Пароль']/following-sibling::input").send_keys("123456")
    
    button = WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH ,"//button[text()='Войти']")))
    button.click()

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Оформить заказ']")))

    driver.find_element(By.XPATH , "//p[text()='Личный Кабинет']").click()

    logout_button = wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Выход']")))
    assert logout_button.is_displayed()


def test_login_via_registration_form_link(driver):

    wait = WebDriverWait(driver, 5)

    driver.find_element(By.XPATH , "//button[text()='Войти в аккаунт']").click()
    driver.find_element(By.CSS_SELECTOR , "a[href='/register']").click()
    
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH , "//a[@href='/login']"))).click()

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//label[text()='Email']")))
    driver.find_element(By.XPATH , "//label[text()='Email']/following-sibling::input").send_keys("ekaterinaaboimova45777@yandex.ru")
    driver.find_element(By.XPATH , "//label[text()='Пароль']/following-sibling::input").send_keys("123456")
    
    button = wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Войти']")))
    button.click()

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Оформить заказ']")))
    driver.find_element(By.XPATH , "//p[text()='Личный Кабинет']").click()

    logout_button = wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Выход']")))
    assert logout_button.is_displayed()