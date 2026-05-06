from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_logout_from_personal_account(driver,login):

    wait =  WebDriverWait(driver, 5)

    wait.until(expected_conditions.element_to_be_clickable((By.XPATH ,"//p[text()='Личный Кабинет']"))).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Выход']"))).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Войти']")))
    
    assert driver.find_element(By.XPATH ,"//button[text()='Войти']").is_displayed()