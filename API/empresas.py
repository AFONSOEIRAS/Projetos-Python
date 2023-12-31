import pandas as pd

# Substitua 'seu_arquivo.csv' pelo caminho do seu arquivo CSV
caminho_arquivo =  r'C:\Users\afons\OneDrive\Área de Trabalho\ESTABELE.CSV'

# Leitura do arquivo CSV ignorando linhas com erros

dados = pd.read_csv(caminho_arquivo, encoding='latin-1', on_bad_lines='skip')
# Trabalhe com os dados aqui
print(dados.head())  # Exemplo: exibe as primeiras linhas dos dados