import os
import hashlib
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import zipfile

def decrypt_file(input_file, output_file, password):
    # Ler os dados criptografados do arquivo
    with zipfile.ZipFile(input_file, 'r') as zf:
        encrypted_data = zf.read('data')

    # Extrair o vetor de inicialização e os dados criptografados
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]

    # Calcular o hash SHA-256 da senha
    hash_obj = hashlib.sha256()
    hash_obj.update(password.encode())
    key = hash_obj.digest()

    # Criar um objeto Cipher para descriptografar os dados
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Descriptografar os dados
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Remover o padding
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()

    # Escrever os dados descriptografados para o arquivo de saída
    with open(output_file, 'wb') as f:
        f.write(decrypted_data)

# Exemplo de uso
input_file = 'arquivo_criptografado.zip'
output_file = 'arquivo_descriptografado.rar'
password = '1$4B3ll4'

decrypt_file(input_file, output_file, password)


