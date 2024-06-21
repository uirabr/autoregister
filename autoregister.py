from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


# Definindo o driver do Selenium
service = Service(ChromeDriverManager().install())
print(service)

navegador = webdriver.Chrome(service=service)
navegador.implicitly_wait(0.3)

# Passo 1: Abrir a página web
navegador.get("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
time.sleep(3)

# Passo 2: Fazer login
elemento_id = navegador.find_element(By.ID, "email")
elemento_id.click()
elemento_id.send_keys("pythonimpressionador@gmail.com")

elemento_id = navegador.find_element(By.ID, "password")
elemento_id.click()
elemento_id.send_keys("senha")

elemento_id = navegador.find_element(By.ID, "pgtpy-botao")
elemento_id.click()


# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("d:\Codes\Python\JornadaPython\Automacao\produtos.csv")

print(tabela)

nome_colunas = ["codigo", "marca", "tipo", "categoria", "preco_unitario", "custo", "obs"]

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    for coluna in nome_colunas:
        elemento_id = navegador.find_element(By.ID, coluna)
        elemento_id.click()
        elemento_id.send_keys(str(tabela.loc[linha, coluna]))

    elemento_id = navegador.find_element(By.ID, "pgtpy-botao")
    elemento_id.click()
    time.sleep(0.1)
    navegador.execute_script("window.scrollTo(0, 0)")

time.sleep(60)

navegador.quit()
