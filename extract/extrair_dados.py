# Este script extrai dados de uma URL e salva em um arquivo local.
# %%
import requests# biblioteca para fazer requisições HTTP
# %%
import os
# %%
def extrair_dados(url,destino):# função para extrair dados de uma URL e salvar em um arquivo
    reposta = requests.get(url)
    with open(destino, 'wb') as f:
        f.write(reposta.content) 
        print(f"Dados salvos em {destino}")  
url = "https://filesamples.com/samples/document/xlsx/sample1.xlsx"# URL do arquivo a ser baixado
destino = "dados/raw/sample1.xlsx"# caminho onde o arquivo será salvo
os.makedirs("dados/raw", exist_ok=True)# cria o diretório se não existir
extrair_dados(url, destino)# chama a função para extrair os dados