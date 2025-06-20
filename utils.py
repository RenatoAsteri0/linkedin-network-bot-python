# linkedin_bot/utils.py

from datetime import datetime


def gerar_saudacao(nome):
    hora = datetime.now().hour
    if hora < 12:
        saudacao = "Bom dia"
    elif hora < 18:
        saudacao = "Boa tarde"
    else:
        saudacao = "Boa noite"

    return f"{saudacao} {nome}! vi seu perfil e achei legal me conectar. Obrigado!!"
