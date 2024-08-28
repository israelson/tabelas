import polars as pl

def create_filtered_table():
    try:
        # Leitura dos arquivos CSV usando polars
        df1 = pl.read_csv("tab_cad.csv")
        df2 = pl.read_csv("Lotes.csv")
        
        # Remoção dos pontos e traço da coluna 'p.num_cpf_pessoa' e 'CPF'
        df1 = df1.with_column(
            'p.num_cpf_pessoa', 
            df1['p.num_cpf_pessoa'].str.replace(r'\.|-', '')
        )
        df2 = df2.with_column(
            'CPF', 
            df2['CPF'].str.replace(r'\.|-', '')
        )
        
        # Realização da junção
        result_df = df1.inner_join(df2, 'p.num_cpf_pessoa', 'CPF')
        
        # Salvamento do resultado em um novo arquivo CSV
        result_df.write_csv("resultado.csv", separator=";")
    except Exception as e:
        print(f"Erro durante a execução: {e}")

create_filtered_table()









