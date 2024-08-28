import pandas as pd
from datetime import datetime

# Função para calcular a idade com base na data de nascimento
def calcular_idade(data_nascimento):
    hoje = datetime.today()
    nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    return idade

# Carregar o arquivo CSV para um DataFrame, tratando exceções
file_path = 'cecad_criptografado.csv'  # Substitua pelo caminho do seu arquivo CSV
linhas_validas = []

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        try:
            linhas_validas.append(line.strip().split(','))
        except:
            pass

# Verificar se as linhas válidas têm pelo menos 3 colunas (cd_ibge, p.dta_nasc_pessoa, d.marc_pbf)
if len(linhas_validas[0]) >= 3:
    data = pd.DataFrame(linhas_validas[1:], columns=linhas_validas[0])

    # Calcular a idade para todas as entradas
    data['idade'] = data['p.dta_nasc_pessoa'].apply(calcular_idade)

    # Filtrar pessoas entre 12 e 18 anos e que fazem parte do programa PBF
    filtro_idade = (data['idade'] >= 12) & (data['idade'] <= 18)
    filtro_pbf = data['d.marc_pbf'] == '1'  # Considerando que '1' significa pertencer ao programa Bolsa Família
    pessoas_filtradas = data[filtro_idade & filtro_pbf]

    # Agrupar os dados filtrados por cidade e contar o número total de pessoas e o número de pessoas no programa PBF
    grupo_cidade = pessoas_filtradas.groupby('cd_ibge')
    resultado = []

    for cidade, cidade_data in grupo_cidade:
        total_pessoas = len(cidade_data)
        pessoas_pbf = len(cidade_data)
        resultado.append({'cidade': cidade, 'total_pessoas': total_pessoas, 'pessoas_pbf': pessoas_pbf})

    # Exibir os resultados
    for r in resultado:
        print(f"Na cidade de {r['cidade']}:")
        print(f"Total de pessoas entre 12 e 18 anos cadastradas: {r['total_pessoas']}")
        print(f"Total de pessoas entre 12 e 18 anos no programa PBF: {r['pessoas_pbf']}")
        print("-----------------------")
else:
    print("O arquivo não possui as colunas necessárias.")
