import os
import json
import pandas as pd

# Diretório que contém os arquivos JSON
diretorio = r'C:\Files\INDICADORES DE LEITURAS - COPASA\DATABASE\MG'

# Inicializa um DataFrame vazio para armazenar todos os dados
dados_totais = pd.DataFrame()

# Itera sobre cada arquivo no diretório
for nome_arquivo in os.listdir(diretorio):
    # Verifica se o arquivo é um arquivo JSON
    if nome_arquivo.endswith('.json'):
        # Caminho completo para o arquivo
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        print(f"Processando {nome_arquivo}")
        
        # Abre o arquivo JSON
        with open(caminho_arquivo, encoding='utf-8') as arquivo:    
            dados = json.load(arquivo)  # Decodifica os dados

        # Converte os dados JSON em um DataFrame do pandas
        df = pd.json_normalize(dados, 'features')

        # Adiciona a coluna "Municipio" com o nome do arquivo (sem a extensão .json)
        df['Municipio'] = nome_arquivo[:-5]

        # Concatena o DataFrame atual com os dados totais
        dados_totais = pd.concat([dados_totais, df])

# Salva os dados totais como um arquivo CSV
dados_totais.to_csv(r'C:\Files\INDICADORES DE LEITURAS - COPASA\DATABASE\csvfile.csv', encoding='utf-8', index=False)
print("Arquivo gerado!")


