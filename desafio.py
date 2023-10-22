import pandas as pd

# Dados do desafio
dados_desafio = {
    'ID': [1, 2, 3],
    'Nome': ['Vania', 'Thayna', 'Pryscilla']
    
}

# Extração dos dados do desafio (Extract)
df = pd.DataFrame(dados_desafio)

# Etapa de Transformação (Transform)
df['mensagem'] = 'Olá ' + df['Nome'] + ', obrigada por participar desse Bootcamp!'

# Etapa de Carregamento (Load)
df.to_excel('Projeto_ETL.xlsx', index=False)

# Exibir o DataFrame resultante
print(df)