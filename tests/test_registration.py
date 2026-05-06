from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_successful_registration_with_valid_data(driver,name,email,password):

    wait =  WebDriverWait(driver, 5)

    driver.find_element(By.XPATH , "//button[text()='Войти в аккаунт']").click()
    driver.find_element(By.CSS_SELECTOR , "a[href='/register']").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH , "//button[text()='Зарегистрироваться']")))

    driver.find_element(By.XPATH , "//label[text()='Имя']/following-sibling::input").send_keys(name)
    driver.find_element(By.XPATH , "//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH , "//label[text()='Пароль']/following-sibling::input").send_keys(password)
    driver.find_element(By.XPATH , "//button[text()='Зарегистрироваться']").click()

    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//h2[text()='Вход']")))
    assert driver.find_element(By.XPATH , "//h2[text()='Вход']").is_displayed()


def test_registration_fails_with_invalid_password(driver):

    wait =  WebDriverWait(driver, 5)

    driver.find_element(By.XPATH , "//button[text()='Войти в аккаунт']").click()
    driver.find_element(By.CSS_SELECTOR , "a[href='/register']").click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH , "//button[text()='Зарегистрироваться']")))

    driver.find_element(By.XPATH , "//label[text()='Имя']/following-sibling::input").send_keys("Екатерина")
    driver.find_element(By.XPATH , "//label[text()='Email']/following-sibling::input").send_keys("ekaterinaaboimova45777@yandex.ru")
    driver.find_element(By.XPATH , "//label[text()='Пароль']/following-sibling::input").send_keys("12345")
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH , "//button[text()='Зарегистрироваться']"))).click()

    error = driver.find_element(By.XPATH , "//p[text()='Некорректный пароль']")
    assert error.is_displayed()