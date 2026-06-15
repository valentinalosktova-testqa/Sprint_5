from selenium.webdriver.common.by import By

class StellarLocators:
    # Поле "Имя"
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")

    # Поле "Email"
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")

    #пароль
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")

    #кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")

    #сообщение об ошибке
    PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")

    # Ссылка "Личный Кабинет"
    LOGIN_LINK = (By.LINK_TEXT, "Личный Кабинет")

    # Ссылка "Зарегистрироваться"
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")

    # Кнопка "Войти в аккаунт" на главной
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Ссылка "Восстановить пароль"
    FORGOT_PASSWORD_LINK = (By.LINK_TEXT, "Восстановить пароль")

    # Кнопка "Войти" (на формах)
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    # Ссылка на логотип (кликабельная область, ведущая на главную)
    LOGO_LINK = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a")

    # Ссылка "Войти" на формах (регистрация, восстановление)
    LOGIN_LINK_ON_FORM = (By.LINK_TEXT, "Войти")
    
