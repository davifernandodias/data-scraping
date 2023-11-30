from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import pandas as pd

# Configurando o driver do Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\ppedr\OneDrive\Área de Trabalho\davi estudo\APS\downalod"}) 
driver = webdriver.Chrome(options=options)

# URL da página
url = "https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx"

# Abre a página no navegador
driver.get(url)

# Selecionar furtos de veículos
furtos_veiculos = driver.find_element(By.ID, "cphBody_btnFurtoVeiculo")
furtos_veiculos.click()

anos = [22]
meses = [12]



# Lista para armazenar os dados
dados = []

for ano in anos:
    sel_ano = driver.find_element(By.ID, f"cphBody_lkAno{ano}")
    sel_ano.click()
    for mes in meses:
        sel_mes = driver.find_element(By.ID, f"cphBody_lkMes{mes}")
        sel_mes.click()
        btn_exportar = driver.find_element(By.ID, "cphBody_ExportarBOLink")
        btn_exportar.click()

        # Esperar até que o arquivo seja baixado completamente (aguarda até 60 segundos)
        tempo_espera = 0
        while not os.path.exists(r"C:\Users\ppedr\OneDrive\Área de Trabalho\davi estudo\APS\downalod\DadosBO_20"+ str(ano) + "_"+str(mes) + "(FURTO DE VEÍCULOS).xls"):
            time.sleep(1)
            tempo_espera += 1


for ano in anos:
    for mes in meses:
        pathname = r"C:\Users\ppedr\OneDrive\Área de Trabalho\davi estudo\APS\downalod\DadosBO_20"+ str(ano) + "_"+str(mes) + "(FURTO DE VEÍCULOS).xls"
        if os.path.exists(pathname):
            read_file  = pd.read_csv(pathname)
            read_file.to_csv(r"C:\Users\ppedr\OneDrive\Área de Trabalho\davi estudo\APS\downalod\csv\DadosBO_20"+ str(ano) + "_"+str(mes) + "(FURTO DE VEÍCULOS).csv", index= None, header= True)
            
            
        # Carregar os dados do arquivo CSV usando pandas
#       if os.path.exists(r"C:\Users\cadug\OneDrive\Imagens\Faculdade\dados.csv"):
#          df = pd.read_csv(r"C:\Users\cadug\OneDrive\Imagens\Faculdade\dados.csv", sep=';', encoding='latin1')
#          dados.append(df)

# Combinar todos os DataFrames em um único DataFrame
#dados_completos = pd.concat(dados, ignore_index=True)

# Salvar os dados como um arquivo CSV
#dados_completos.to_csv('dados_completos.csv', index=False)

# Fechar o navegador
driver.quit()