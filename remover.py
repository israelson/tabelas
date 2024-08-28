import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('corrigido.csv')

# Função para remover o '.0' dos números da coluna
def remove_decimal(num):
    num_str = str(num)
    if num_str.endswith('.0') and num_str != '0.0':
        return num_str[:-2]
    return num_str

# Aplicar a função à coluna desejada
df['nis'] = df['nis'].apply(remove_decimal)

# Salvar os dados em um novo arquivo CSV
df.to_csv('limpa.csv', index=False)