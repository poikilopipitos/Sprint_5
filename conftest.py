import random
import pytest
from selenium import webdriver
import time
import locators

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
    unique_digits = int(time.time() * 1000) % 1000
    email = 'ekaterinaaboimova' + str(unique_digits) + '@yandex.ru'
    return email


@pytest.fixture
def password():
    password = str(random.randint(100000,999999))
    return password

@pytest.fixture(scope="session")
def registered_user():
    driver = webdriver.Chrome()
    unique_digits = int(time.time() * 1000) % 1000
    email = 'ekaterinaaboimova' + str(unique_digits) + '@yandex.ru'
    password = str(random.randint(100000,999999))
    driver.get("https://stellarburgers.education-services.ru/register")
    driver.find_element(*locators.NAME_INPUT).send_keys("Ekaterina")
    driver.find_element(*locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*locators.REGISTER_BUTTON).click()
    time.sleep(1)
    driver.quit()
    return email, password











