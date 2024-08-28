import pandas as pd
from tqdm import tqdm

# Lê o arquivo CSV ignorando linhas com erros
with open('tab_cad_13072024_11_20240806.csv', 'r', encoding='utf-8', errors='ignore') as file:
    total_lines = sum(1 for line in file)

# Inicializa a barra de progresso
bar = tqdm(total=total_lines, desc='Lendo CSV')

# Lista para armazenar os pedaços do DataFrame
chunks = []

# Lê o arquivo CSV
with open('tab_cad_13072024_11_20240806.csv', 'r', encoding='utf-8', errors='ignore') as file:
    df = pd.read_csv(file, delimiter=';', iterator=True, low_memory=False)
    for chunk in df:
        # Adiciona cada pedaço à lista
        chunks.append(chunk)
        # Atualiza a barra de progresso a cada chunk lido
        bar.update(len(chunk))

# Fecha a barra de progresso
bar.close()

# Concatena todos os pedaços em um único DataFrame
df = pd.concat(chunks, ignore_index=True)

# Lê os nomes das colunas do arquivo de texto
with open('colunas.txt', 'r') as file:
    colunas_desejadas = [coluna.strip() for coluna in file]

# Verifica se há colunas desejadas
if colunas_desejadas:
    # Verifica se as colunas desejadas estão presentes no DataFrame
    colunas_validas = [coluna for coluna in colunas_desejadas if coluna in df.columns]

    if colunas_validas:
        # Seleciona as colunas desejadas
        df_selecionado = df[colunas_validas]

        # Salva as colunas selecionadas em outro arquivo CSV
        df_selecionado.to_csv('prato.csv', sep=';', index=False, float_format='%.0f')  # index=False para não salvar o índice do DataFrame
    else:
        print("Nenhuma das colunas desejadas está presente no DataFrame.")
else:
    print("Nenhuma coluna desejada encontrada no arquivo de texto.")




df_selecionado.to_csv('prato.csv', sep=';', index=False, float_format='%.0f')

