import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")
    yield driver
    driver.quit()

@pytest.fixture
def name():
    names = ["Александр", "Екатерина", "Иван", "Мария", "Дмитрий", "Анна", "Сергей", "Ольга"]
    name = random.choice(names)
    return name

@pytest.fixture
def email():
    email = 'stellaburgers' + str(random.randint(100,999)) + '@yandex.ru'
    return email


@pytest.fixture
def password():
    password = str(random.randint(100000,999999))
    return password


@pytest.fixture
def login(driver):

    login_button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Войти в аккаунт']")))
    login_button.click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH ,"//label[text()='Email']")))
    driver.find_element(By.XPATH , "//label[text()='Email']/following-sibling::input").send_keys("ekaterinaaboimova45777@yandex.ru")
    driver.find_element(By.XPATH , "//label[text()='Пароль']/following-sibling::input").send_keys("123456")

    button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH ,"//button[text()='Войти']")))
    button.click()

    yield driver
    driver.quit()








