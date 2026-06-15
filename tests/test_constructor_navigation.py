from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_unique_email

def test_go_to_constructor_via_logo(driver):
    driver.get('https://stellarburgers.education-services.ru/')

    # Клик по ссылке "Личный Кабинет"
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

    # На странице логина клик по ссылке "Зарегистрироваться"
    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

    # Генерация уникального email
    email = generate_unique_email()

    driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input").send_keys("Валентина")
    driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("123456")

    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()

    wait = WebDriverWait(driver, 3)
    wait.until(EC.url_contains("login"))
    assert "login" in driver.current_url

        # Вход как зарегистрированный пользователь
    driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("123456")
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    driver.find_element(By.XPATH, "(//a[@href='/'])[1]").click()

    # Проверить, что мы на главной (URL не содержит account)
    assert driver.current_url == "https://stellarburgers.education-services.ru/"


def test_go_to_constructor_via_constructor_button(driver):
    driver.get('https://stellarburgers.education-services.ru/')

    # Авторизация (копируем ту же логику, что в первом тесте)
    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()
    email = generate_unique_email()
    driver.find_element(By.XPATH, ".//label[text()='Имя']/following-sibling::input").send_keys("Валентина")
    driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("123456")
    driver.find_element(By.XPATH, ".//button[text()='Зарегистрироваться']").click()
    wait = WebDriverWait(driver, 3)
    wait.until(EC.url_contains("login"))
    assert "login" in driver.current_url
    driver.find_element(By.XPATH, ".//label[text()='Email']/following-sibling::input").send_keys(email)
    driver.find_element(By.XPATH, ".//label[text()='Пароль']/following-sibling::input").send_keys("123456")
    driver.find_element(By.XPATH, ".//button[text()='Войти']").click()

    # Клик по кнопке «Конструктор»
    driver.find_element(By.LINK_TEXT, "Конструктор").click()

    # Проверяем, что мы на главной странице
    assert driver.current_url == "https://stellarburgers.education-services.ru/"

