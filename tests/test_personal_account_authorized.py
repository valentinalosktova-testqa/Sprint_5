from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_unique_email
from pages.locators import StellarLocators
from urls import BASE_URL


class TestPersonalAccountAuthorized:

    def test_personal_account_authorized(self, driver):
        driver.get(BASE_URL)
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

        # Проверяем, что открылась страница /account
        wait.until(EC.url_contains("account"))
        assert "account" in driver.current_url