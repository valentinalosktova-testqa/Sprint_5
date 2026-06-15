from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_unique_email
from pages.locators import StellarLocators

class TestLogout:

    def test_logout(self, driver):
        driver.get('https://stellarburgers.education-services.ru/')

        # Регистрация нового пользователя
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

        email = generate_unique_email()
        driver.find_element(*StellarLocators.NAME_INPUT).send_keys("Валентина")
        driver.find_element(*StellarLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*StellarLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*StellarLocators.REGISTER_BUTTON).click()

        wait = WebDriverWait(driver, 3)
        wait.until(EC.url_contains("login"))
        assert "login" in driver.current_url

        # Вход как зарегистрированный пользователь
        driver.find_element(*StellarLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*StellarLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*StellarLocators.LOGIN_BUTTON).click()

        # Переход в личный кабинет
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

        # Клик по кнопке «Выйти» с явным ожиданием
        wait = WebDriverWait(driver, 5)
        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[text()='Выход']")))
        logout_button.click()

        # Проверяем, что открылась страница /login
        wait.until(EC.url_contains("login"))
        assert "login" in driver.current_url