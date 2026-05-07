from selenium.webdriver.common.by import By

LOGIN_ACCOUNT_BUTTON = (By.XPATH , "//button[text()='Войти в аккаунт']")            #Войти в аккаунт
REGISTER_LINK = (By.CSS_SELECTOR , "a[href='/register']")                           #Сссылка Зарегистрироваться
REGISTER_BUTTON = (By.XPATH , "//button[text()='Зарегистрироваться']")              #Кнопка Зарегистрироваться
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following::input[1]")                #Поле Имя для регистрации
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following::input[1]")             #Поле Email для регистрации
EMAIL_INPUT_TITLE = (By.XPATH , "//label[text()='Email']")                          #Поле Email/плейсхолдер
PASSWORD_INPUT = (By.XPATH , "//input[@name='Пароль']")                             #Поле Пароль
LOGIN_TITLE = (By.XPATH , "//h2[text()='Вход']")                                    #Заголовок Вход
INVALID_PASSWORD_ERROR = (By.XPATH , "//p[text()='Некорректный пароль']")           #Ошибка Некорректный пароль
PLACE_ORDER_BUTTON = (By.XPATH , "//button[text()='Оформить заказ']")               #Кнопка Оформить заказ
PERSONAL_ACCOUNT_BUTTON = (By.XPATH , "//p[text()='Личный Кабинет']")               #Личный Кабинет
LOGOUT_BUTTON = (By.XPATH , "//button[text()='Выход']")                             #Кнопка Выход
LOGIN_BUTTON = (By.XPATH , "//button[text()='Войти']")                              #Кнопка Войти на странице авторизации
FORGOT_PASSWORD_LINK = (By.XPATH , "//a[@href='/forgot-password']")                 #Ссылка Восстановить пароль
CONSTRUCTOR_LINK = (By.XPATH , "//p[text()='Конструктор']")                         #Ссылка Конструктор
BUNS_TAB = (By.XPATH , "//span[text()='Булки']")                                    #Булки
ACTIVE_BUNS_TAB = (By.XPATH , "//h2[text()='Булки']")                               # Активная вкладка Булки
SAUCES_TAB = (By.XPATH , "//span[text()='Соусы']")                                  #Соусы
ACTIVE_SAUCES_TAB = (By.XPATH , "//h2[text()='Соусы']")                             # Активная вкладка Соусы
FILLINGS_TAB = (By.XPATH , "//span[text()='Начинки']")                              #Начинки
ACTIVE_FILLINGS_TAB = (By.XPATH , "//h2[text()='Начинки']")                         # Активная вкладка Начинки
HEADER_LOGO = (By.CLASS_NAME ,'AppHeader_header__logo__2D0X2')                      #Логотип
LOGIN_LINK = (By.XPATH , "//a[@href='/login']")                                     #Заголовок Вход/
EMAIL_INPUT_AUTORISATION = (By.XPATH , "//input[@name='name']")                     #Поле Email для авторизации

