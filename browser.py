# linkedin_bot/browser.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


class Browser:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--disable-notifications")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument("--disable-blink-features=AutomationControlled")

    def start(self):
        print("🧠 Iniciando navegador Chorme...")
        service = Service(executable_path="C:/Users/renat/OneDrive/Pessoal/Profissao/python/pythonprojects/portifolio_emprego/chromedriver.exe")
        driver = webdriver.Chrome(service=service, options=self.options)
        driver.implicitly_wait(10)
        return driver
