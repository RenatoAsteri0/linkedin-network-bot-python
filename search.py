# linkedin_bot/search.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Search:
    def __init__(self, driver):
        self.driver = driver

    def buscar(self, palavra_chave):
        print(f"🔍 Buscando perfis com a palavra-chave: {palavra_chave}")

        # Navegar até a página de busca de pessoas do LinkedIn
        self.driver.get("https://www.linkedin.com/search/results/people/")
        time.sleep(3)

        # Localizar a barra de busca
        barra_busca = self.driver.find_element(By.XPATH, "//input[contains(@placeholder, 'Pesquisar')]")
        barra_busca.clear()
        barra_busca.send_keys(palavra_chave)
        barra_busca.send_keys(Keys.RETURN)

        time.sleep(5)  # Espera carregar resultados


        print("✅ Busca concluída.")

