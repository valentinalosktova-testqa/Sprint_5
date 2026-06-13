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
    
