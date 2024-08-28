import pandas as pd

# Carregar os CSVs
tabela1 = pd.read_csv('Beneficiarios Prato Fácil.csv', delimiter=';')
tabela2 = pd.read_csv('vencer.csv', delimiter=';')


# Garantir que a coluna NIS está como string em ambas as tabelas
tabela1['NIS'] = tabela1['NIS'].astype(str)
tabela2['NIS'] = tabela2['NIS'].astype(str)


# Fazer o merge das tabelas com base na coluna NIS, mantendo apenas os registros que estão na tabela 1
merged = pd.merge(tabela1, tabela2, on='NIS', how='inner')


# Faixas salariais
salario_faixas = {
    'Até 700': merged[merged['d.vlr_renda_media_fam'] <= 700].shape[0],
    'Até 1400': merged[(merged['d.vlr_renda_media_fam'] > 700) & (merged['d.vlr_renda_media_fam'] <= 1400)].shape[0],
    'Mais de 1400': merged[merged['d.vlr_renda_media_fam'] > 1400].shape[0]
}

# Exibir os resultados

print("\nContagem por faixa salarial:")
print(salario_faixas)
