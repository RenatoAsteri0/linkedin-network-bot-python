# linkedin_bot/connect.py

import time
from selenium.webdriver.common.by import By
from utils import gerar_saudacao


class Connect:
    def __init__(self, driver):
        self.driver = driver

    def enviar_convites(self, max_convites):
        print(f"📬 Enviando até {max_convites} convites...")

        conectados = 0
        botoes = self.driver.find_elements(By.XPATH, "//button[contains(@aria-label, 'Convidar')]")

        for botao in botoes:
            try:
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", botao)
                time.sleep(1)
                self.driver.execute_script("arguments[0].click();", botao)
                time.sleep(2)

                # Extrair o nome diretamente do botão
                nome_completo = botao.get_attribute("aria-label").replace("Convidar", "").replace("para se conectar", "").strip()
                print(f"➡️ Conectando com {nome_completo}")

                # Clicar em “Adicionar nota”
                botao_nota = self.driver.find_element(By.XPATH, "//button[@aria-label='Adicionar nota']")
                botao_nota.click()
                time.sleep(1)

                # Gerar saudação
                mensagem = gerar_saudacao(nome_completo)

                # Escrever mensagem
                campo_mensagem = self.driver.find_element(By.ID, "custom-message")
                campo_mensagem.clear()
                campo_mensagem.send_keys(mensagem)

                botao_enviar = self.driver.find_element(By.XPATH, "//button[@aria-label='Enviar convite']")
                self.driver.execute_script("arguments[0].click();", botao_enviar)

                print(f"✅ Convite enviado para: {nome_completo}")
                conectados += 1
                time.sleep(2)

                if conectados >= max_convites:
                    break

            except Exception as e:
                print("⚠️ Erro ao tentar conectar:", e)
                # Fecha modal, se necessário
                try:
                    fechar = self.driver.find_element(By.XPATH, "//button[@aria-label='Fechar']")
                    fechar.click()
                    time.sleep(1)
                except:
                    pass
                continue

        print(f"🔚 Total de convites enviados: {conectados}")
