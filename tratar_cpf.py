import pandas as pd

# Carregar o arquivo CSV
df = pd.read_csv('mulher protegida.csv')

# Remover pontos e traços da coluna de CPF (supondo que a coluna se chame 'CPF')
df['CPF'] = df['CPF'].str.replace('.', '').str.replace('-', '')

# Salvar o arquivo CSV apenas com a coluna de CPFs formatados
df[['CPF']].to_csv('seu_arquivo_formatado.csv', index=False)
