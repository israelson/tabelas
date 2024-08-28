import pandas as pd
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from tqdm import tqdm

def encrypt_aes(text, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=get_random_bytes(16))
    ciphertext = cipher.encrypt(pad(text.encode('utf-8'), AES.block_size))
    return ciphertext.hex()

def decrypt_aes(ciphertext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=get_random_bytes(16))
    decrypted_text = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), AES.block_size)
    return decrypted_text.decode('utf-8')

def encrypt_with_key(value, key):
    if pd.notna(value):
        if pd.api.types.is_numeric_dtype(value):
            return encrypt_aes(str(int(value)), key)  # Converte para int para remover o .0
        else:
            return encrypt_aes(str(value), key)
    else:
        return value


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

def encrypt_columns(df, columns, key):
    for coluna in columns:
        tqdm.pandas(desc=f"Criptografando coluna '{coluna}'")
        df[coluna] = df[coluna].progress_apply(lambda x: encrypt_with_key(x, key))
    return df

def main():
    caminho_arquivo = '2024 - BASE CADÚNICO/tab_cad_16122023_11_20240109.csv'
    colunas_para_criptografar = ['p.nom_pessoa', 'p.num_nis_pessoa_atual', 'p.dta_nasc_pessoa', 'p.num_cpf_pessoa']

    # Gerar uma chave (isso deve ser feito uma vez e mantido em segredo)
    chave_secreta = get_random_bytes(32)

    df = read_csv_file(caminho_arquivo)

    if df is not None:
        df = encrypt_columns(df, colunas_para_criptografar, chave_secreta)
        df.to_csv('cecad_criptografado3.csv', index=False, sep=';')
        print(chave_secreta)
        print("TERMINOU")

if __name__ == "__main__":
    main()
