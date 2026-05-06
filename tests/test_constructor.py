from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_switch_to_buns_section(driver,login):

    wait =  WebDriverWait(driver, 5)
    
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH , "//span[text()='Соусы']"))).click()
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH , "//span[text()='Булки']"))).click()
    wait.until(expected_conditions.visibility_of_element_located((By.XPATH , "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Булки']")))

    assert driver.find_element(By.XPATH , "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Булки']").is_displayed()


def test_switch_to_fillings_section(driver,login):
    
    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH , "//span[text()='Начинки']"))).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH , "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Начинки']")))
    
    assert driver.find_element(By.XPATH , "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Начинки']").is_displayed()


def test_switch_to_sauces_section(driver,login):

    WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH , "//span[text()='Соусы']"))).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH , "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Соусы']")))
    
    assert driver.find_element(By.XPATH , "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Соусы']").is_displayed()  