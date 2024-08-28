import polars as pl

# Carregar o arquivo CSV com os números de cadastro
df_numeros = pl.read_csv('vencer_cpf.csv')

# Carregar o arquivo CSV com os dados completos
df_dados = pl.read_csv('tab_cad_13042024_11_20240507.csv')

# Realizar o join utilizando os números de cadastro como chave
df_filtrado = df_dados.join(df_numeros, on='p.num_cpf_pessoa', how='CPF')

# Salvar os dados filtrados em um novo arquivo CSV
df_filtrado.write_csv('filtrados_vencer.csv')

