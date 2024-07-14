# json_to_csv
 Conversão de dados em json para csv

# Processamento de Arquivos JSON de Indicadores de Leituras - COPASA

Este repositório contém um script em Python que processa arquivos JSON de indicadores de leituras, os transforma em um DataFrame do Pandas e salva o resultado final em um arquivo CSV.

## Estrutura do Projeto

```
├── INDICADORES DE LEITURAS - COPASA
│   ├── DATABASE
│   │   ├── MG
│   │   │   ├── arquivo1.json
│   │   │   ├── arquivo2.json
│   │   │   └── ...
│   │   └── csvfile.csv
│   └── script.py
```

## Requisitos

- Python 3.x
- Pandas

Você pode instalar as dependências usando:

```bash
pip install pandas
```

## Como Usar

1. Coloque os arquivos JSON que você deseja processar no diretório `C:\Files\INDICADORES DE LEITURAS - COPASA\DATABASE\MG`.

2. Execute o script `script.py`:

```python
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
```

3. O script irá processar todos os arquivos JSON no diretório especificado, agregar os dados e salvar um arquivo CSV chamado `csvfile.csv` no mesmo diretório.

## Funcionalidades

- **Processamento de Arquivos JSON**: O script processa todos os arquivos JSON em um diretório especificado.
- **Conversão para DataFrame**: Os dados JSON são convertidos em DataFrames do Pandas.
- **Agregação de Dados**: Os DataFrames individuais são concatenados em um único DataFrame.
- **Exportação para CSV**: O DataFrame final é exportado para um arquivo CSV.

## Contribuição

Sinta-se à vontade para abrir issues e enviar pull requests. Toda contribuição é bem-vinda!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
