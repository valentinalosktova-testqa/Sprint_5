from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import StellarLocators
from helpers import generate_unique_email
from urls import BASE_URL

class TestConstructorNavigation:

    def test_go_to_constructor_via_logo(self, driver):
        driver.get(BASE_URL)

        # Клик по ссылке "Личный Кабинет"
        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

        # На странице логина клик по ссылке "Зарегистрироваться"
        driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

        # Генерация уникального email
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

        driver.find_element(*StellarLocators.LOGO_LINK).click()

        # Проверить, что мы на главной (URL не содержит account)
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

    def test_go_to_constructor_via_constructor_button(self, driver):
        driver.get(BASE_URL)

        # Авторизация (копируем ту же логику, что в первом тесте)
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
        driver.find_element(*StellarLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*StellarLocators.PASSWORD_INPUT).send_keys("123456")
        driver.find_element(*StellarLocators.LOGIN_BUTTON).click()

        # Клик по кнопке «Конструктор»
        driver.find_element(By.LINK_TEXT, "Конструктор").click()

        # Проверяем, что мы на главной странице
        assert driver.current_url == "https://stellarburgers.education-services.ru/"

