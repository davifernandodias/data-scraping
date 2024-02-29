from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import pandas as pd

# Configuring Chrome Driver
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\ppedr\OneDrive\Área de Trabalho\davi estudo\APS\downalod"})  # alter directory for you !!!!!!!!
driver = webdriver.Chrome(options=options)

# URL page
url = "https://www.ssp.sp.gov.br/transparenciassp/Consulta2022.aspx"

# Get page of WEB
driver.get(url)

# Select car theft
furtos_veiculos = driver.find_element(By.ID, "cphBody_btnFurtoVeiculo")
furtos_veiculos.click()

anos = [22]
meses = [12]



# List for get data
dados = []

for ano in anos:
    sel_ano = driver.find_element(By.ID, f"cphBody_lkAno{ano}")
    sel_ano.click()
    for mes in meses:
        sel_mes = driver.find_element(By.ID, f"cphBody_lkMes{mes}")
        sel_mes.click()
        btn_exportar = driver.find_element(By.ID, "cphBody_ExportarBOLink")
        btn_exportar.click()

        # sleep 30s
        tempo_espera = 0
        while not os.path.exists(r"C:\Users\ppedr\OneDrive\Área de Trabalho\davi estudo\APS\downalod\DadosBO_20"+ str(ano) + "_"+str(mes) + "(FURTO DE VEÍCULOS).xls"):
            time.sleep(1)
            tempo_espera += 1


for ano in anos: # convert xlsx to csv
    for mes in meses:
        pathname = r"C:\Users\ppedr\OneDrive\Área de Trabalho\davi estudo\APS\downalod\DadosBO_20"+ str(ano) + "_"+str(mes) + "(FURTO DE VEÍCULOS).xls"
        if os.path.exists(pathname):
            read_file  = pd.read_csv(pathname)
            read_file.to_csv(r"C:\Users\ppedr\OneDrive\Área de Trabalho\davi estudo\APS\downalod\csv\DadosBO_20"+ str(ano) + "_"+str(mes) + "(FURTO DE VEÍCULOS).csv", index= None, header= True)
            
            






# exit web
driver.quit()
