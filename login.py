# linkedin_bot/login.py

import time
from selenium.webdriver.common.by import By


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.linkedin.com/login"

    def sign_in(self, email, password):
        print("🔐 Acessando página de login...")
        self.driver.get(self.url)

        # Localiza os campos de e-mail e senha
        email_field = self.driver.find_element(By.ID, "username")
        password_field = self.driver.find_element(By.ID, "password")

        # Preenche os campos
        email_field.send_keys(email)
        password_field.send_keys(password)

        # Clica no botão de login
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        print("✅ Login realizado com sucesso!")
        time.sleep(3)  # Pequena pausa para garantir que a página carregue