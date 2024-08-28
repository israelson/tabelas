import pandas as pd
import hashlib
import numpy as np
from tqdm import tqdm

def encrypt_md5(text):
    if isinstance(text, str):
        md5 = hashlib.md5()
        md5.update(text.encode('utf-8'))
        return md5.hexdigest()
    else:
        return encrypt_md5(str(text))

caminho_arquivo = '2024 - BASE CADÚNICO/tab_cad_16122023_11_20240109.csv'
colunas_para_criptografar = ['p.nom_pessoa', 'p.num_nis_pessoa_atual', 'p.dta_nasc_pessoa', 'p.num_cpf_pessoa']

df = pd.read_csv(caminho_arquivo, sep=';')
df.columns = df.columns.str.strip()

total_linhas = len(df)

for coluna in colunas_para_criptografar:
    tqdm.pandas(desc=f"Criptografando coluna '{coluna}'")
    df[coluna] = df[coluna].progress_apply(encrypt_md5)

df.to_csv('cecad_criptografado.csv', index=False, sep=';')

# Mensagem de término do programa
print("TERMINOU")








