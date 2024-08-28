import pandas as pd
import numpy as np

# Carregar o arquivo CSV
df = pd.read_csv('limpa.csv')

# Converter a coluna 'nis' para float64
df['nis'] = pd.to_numeric(df['nis'], errors='coerce')

# Substituir os valores NaN por valores nulos (None)
df['nis'] = df['nis'].replace(np.nan, None)

# Salvar os dados atualizados em um novo arquivo CSV
df.to_csv('corrigido.csv', index=False)
