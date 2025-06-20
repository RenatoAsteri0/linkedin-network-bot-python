# main.py
import time
from browser import Browser
from login import Login
from search import Search
from connect import Connect
from config import LINKEDIN_EMAIL, LINKEDIN_PASSWORD

def main():
    print("🚀 Iniciando bot de networking no LinkedIn...")

    browser = Browser()
    driver = browser.start()

    login = Login(driver)
    login.sign_in(LINKEDIN_EMAIL, LINKEDIN_PASSWORD)

    search = Search(driver)
    search.buscar("Programador")

    print("✅ Busca finalizada!")
    time.sleep(6)

    connect = Connect(driver)
    connect.enviar_convites(max_convites=2)

if __name__ == "__main__":
    main()