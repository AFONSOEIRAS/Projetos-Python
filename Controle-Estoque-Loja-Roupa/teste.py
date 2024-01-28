from datetime import datetime

def validar_data(data_str):
    try:
        # Tenta converter a string em um objeto de data
        datetime.strptime(data_str, '%d/%m/%Y')
        return True  # A conversão foi bem-sucedida, então a string é uma data válida
    except ValueError:
        return False  # A conversão falhou, então a string não é uma data válida

# Exemplos de strings de data para validar
datas = ['31/12/2021', '29/02/2020', '2024-01-28', '2021/12/31']

# Validar cada string de data
for data in datas:
    if validar_data(data):
        print(f'A string "{data}" é uma data válida.')
    else:
        print(f'A string "{data}" não é uma data válida.')
