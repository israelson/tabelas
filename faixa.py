import pandas as pd

# Carregando o arquivo Excel
df = pd.read_excel('7. Lista CadÚnico - DEZEMBRO DE 2023 - Até 16.12.2023.xlsx')

# Filtragem pela coluna percapita
filtro_percapita = df['percapita'] < 661
df_filtrado_percapita = df[filtro_percapita]

# Salvando o resultado em um novo arquivo Excel
df_filtrado_percapita.to_excel('filtrado_percapita.xlsx', index=False)

# Filtragem pela coluna faixa
faixas_desejadas = [1, 2, 3, 4]
filtro_faixa = df['faixa'].isin(faixas_desejadas)
df_filtrado_faixa = df[filtro_faixa]

# Salvando o resultado em um novo arquivo Excel
df_filtrado_faixa.to_excel('filtrado_faixa.xlsx', index=False)

# Juntando os dois dataframes
df_final = pd.merge(df_filtrado_percapita, df_filtrado_faixa, how='inner', on='cpf')

# Removendo duplicatas pelo CPF
df_final_sem_duplicatas = df_final.drop_duplicates(subset='cpf')

# Salvando o resultado final em um novo arquivo Excel
df_final_sem_duplicatas.to_excel('resultado_final.xlsx', index=False)
