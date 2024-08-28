import pandas as pd

# Carregar o arquivo Excel
df = pd.read_excel('junto.xlsx')

# Unir as colunas desejadas
coluna1 = df['aposentados']
coluna2 = df['media']
colunas_unidas = pd.concat([coluna1, coluna2], ignore_index=True)

# Remover dados duplicados
dados_sem_duplicatas = colunas_unidas.drop_duplicates()

# Criar um novo DataFrame com os dados sem duplicatas
df_novo = pd.DataFrame({'nis': dados_sem_duplicatas})

# Salvar os dados em um novo arquivo Excel
df_novo.to_csv('unidas.csv', index=False)





