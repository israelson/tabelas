import polars as pl
import pandas as pd


#def create_table_nis_retiree():
    #df = pd.read_csv("./unidas.csv", encoding="utf-8", sep=";")
    #dfNisFiltro = df['nis'].dropna().astype(str).str.replace('.0', '')
    #dfNisFiltro.to_csv('nis_limpo.csv')

def create_table_filtered_nis():
    dfCad = pl.read_csv("tab_cad_13042024_11_20240507.csv", separator=";", ignore_errors=True)
    dfNisAposentados = pl.read_csv("vencer_cpf.csv", encoding="ISO-8859-1")
    dfNisAposentados.drop(['NIS'])
    out = dfCad.join(dfNisAposentados,left_on="p.num_nis_pessoa_atual",right_on="NIS")
    out.write_csv("filtrados.csv", separator=";")

#create_table_nis_retiree()

create_table_filtered_nis()

df = pl.read_csv("filtrados.csv",separator=';')
out = df.filter(
    pl.col("p.nom_pessoa").is_not_null()
)
#out = out.drop(['nis'])
out.write_csv("out.csv",separator=";")