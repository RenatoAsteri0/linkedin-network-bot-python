# 🤖 Bot de Automação para Conexões no LinkedIn

Este repositório apresenta um **bot de automação de networking no LinkedIn**, desenvolvido em **Python com Selenium**.  
Com ele, é possível **buscar perfis, enviar solicitações de conexão e adicionar mensagens personalizadas** de forma automatizada — tudo de forma estratégica e controlada.

---

## 📸 Demonstração

> ![Demonstração do bot](https://github.com/RenatoAsteri0/linkedin-network-bot-python/blob/main/2025-06-2109-11-08-ezgif.com-resize.gif?raw=true)


---

## 🚀 Funcionalidades

✅ Acessa o LinkedIn com login automatizado  
✅ Busca perfis usando termos como "desenvolvedor python"  
✅ Clica no botão “Conectar”  
✅ Adiciona uma mensagem personalizada (ex: "(bom dia, boa tarde ou boa noite) (nome da pessoa)! vi seu perfil e achei legal me conectar. Obrigado!!")  
✅ Envia convites automaticamente para múltiplos perfis

---

## 💡 Particularidades do projeto

- 💭 Estou praticando o paradigma **orientado a objetos (OOP)** para estruturar melhor o código e desenvolver raciocínio de projetos maiores.
- 🎯 O número de conexões enviadas pode ser **controlado** com a variável `max_convites`.
- 🧠 Para contornar problemas de **elemento sobreposto** ao clicar no botão "Conectar", usei **JavaScript via Selenium** como solução prática (ver linha 43 de `connect.py`).


## ⚙️ Tecnologias utilizadas

- Python 3.10+
- [Selenium](https://www.selenium.dev/)
- Navegador: Chrome
- WebDriver: ChromeDriver

---

## ⚠️ Aviso legal

Este projeto foi desenvolvido para fins **educacionais e demonstrativos**.  
Evite o uso excessivo ou abusivo de automações em redes sociais. Respeite os termos de uso da plataforma.

