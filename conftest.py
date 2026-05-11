from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
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

@pytest.fixture
def user_data():
    return "ekaterinaaboimova45777@yandex.ru", "123456"












