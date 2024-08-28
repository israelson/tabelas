import polars as pl

def copiar_linhas(planilha1, planilha2):
    # Carregar as planilhas como DataFrames
    with open(planilha1, 'rb') as f1, open(planilha2, 'rb') as f2:
        conteudo1 = f1.read().decode('ISO-8859-1')
        conteudo2 = f2.read().decode('ISO-8859-1')

    df1 = pl.scan_csv(conteudo1)
    df2 = pl.scan_csv(conteudo2)

    # Filtrar linhas da segunda planilha que estão presentes na primeira planilha
    linhas_copiadas = df2.filter(df2['nome'].isin(df1['p.nome_pessoa']))

    return linhas_copiadas

# Substitua 'planilha1.csv' e 'planilha2.csv' pelos nomes reais dos seus arquivos CSV
linhas_copiadas = copiar_linhas('tab_cad_16092023_11_20230919.csv', 'nomes.csv')

# Salvar as linhas copiadas em uma nova planilha
pl.DataFrame.to_csv(linhas_copiadas, 'nova_planilha.csv')





