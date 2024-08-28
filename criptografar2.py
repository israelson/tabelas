import pandas as pd
import hashlib
from tqdm import tqdm

def encrypt_md5(text):
    if isinstance(text, str):
        md5 = hashlib.md5()
        md5.update(text.encode('utf-8'))
        return md5.hexdigest()
    else:
        return encrypt_md5(str(text))

def read_csv_file(file_path, separator=';'):
    try:
        df = pd.read_csv(file_path, sep=separator)
        df.columns = df.columns.str.strip()
        return df
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {file_path}")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")
        return None

def encrypt_columns(df, columns):
    for coluna in columns:
        tqdm.pandas(desc=f"Criptografando coluna '{coluna}'")
        df[coluna] = df[coluna].progress_apply(encrypt_md5)
    return df

def main():
    caminho_arquivo = '2024 - BASE CADÚNICO/tab_cad_16122023_11_20240109.csv'
    colunas_para_criptografar = ['p.nom_pessoa', 'p.num_nis_pessoa_atual', 'p.dta_nasc_pessoa', 'p.num_cpf_pessoa']

    df = read_csv_file(caminho_arquivo)

    if df is not None:
        df = encrypt_columns(df, colunas_para_criptografar)
        df.to_csv('cecad_criptografado2.csv', index=False, sep=';')
        print("TERMINOU")

if __name__ == "__main__":
    main()
