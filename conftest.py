import random
import pytest
from selenium import webdriver


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









