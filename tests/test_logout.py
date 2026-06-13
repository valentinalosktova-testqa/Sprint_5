from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_unique_email

def test_logout():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.education-services.ru/')

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

    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()

    # Ждём и кликаем по кнопке «Выход»
    wait.until(EC.element_to_be_clickable((By.XPATH, ".//button[text()='Выход']"))).click()

    wait.until(EC.url_contains("login"))
    assert "login" in driver.current_url

    driver.quit()
    
