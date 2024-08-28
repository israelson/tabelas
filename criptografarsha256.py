import os
import hashlib
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import zipfile

def encrypt_file(input_file, output_file, password):
    # Ler o conteúdo do arquivo de entrada
    with open(input_file, 'rb') as f:
        file_data = f.read()

    # Calcular o hash SHA-256 da senha
    hash_obj = hashlib.sha256()
    hash_obj.update(password.encode())
    key = hash_obj.digest()

    # Adicionar padding aos dados do arquivo
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(file_data) + padder.finalize()

    # Criar um vetor de inicialização para o modo CBC
    iv = os.urandom(16)

    # Criar um objeto Cipher para criptografar os dados
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Criptografar os dados
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Escrever os dados criptografados para o arquivo de saída
    with zipfile.ZipFile(output_file, 'w') as zf:
        zf.writestr('data', iv + encrypted_data)

# Exemplo de uso
input_file = 'novo_arquivo.rar'
output_file = 'arquivo_criptografado.rar'
password = '1$4B3ll4'

encrypt_file(input_file, output_file, password)

