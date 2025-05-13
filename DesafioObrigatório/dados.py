import pandas as pd
import numpy as np

# Criar DataFrame com dados hipotéticos
data = {
    "Região": ["Norte", "Norte", "Sul", "Sul", "Norte"],
    "Mês": ["Jan", "Fev", "Jan", "Fev", "Mar"],
    "Vendas": [1500, np.nan, 2200, 1800, 2000],
    "Despesas": [300, 250, np.nan, 400, 350]
}

df = pd.DataFrame(data)

# Salvar em Excel
df.to_excel("vendas.xlsx", index=False, engine="openpyxl")

print("Arquivo 'vendas.xlsx' criado com sucesso!")


# PASSO 1: Carregar e inspecionar os dados
print("\n--- PASSO 1: Carregando e inspecionando os dados ---")

# Carrega o arquivo vendas.xlsx
df = pd.read_excel("vendas.xlsx")

# Mostra as primeiras linhas e informações
print("\nDados originais:")
print(df.head())

print("\nInformações do DataFrame:")
print(df.info())

print("\nValores ausentes (NA/NaN):")
print(df.isna().sum())


# PASSO 2: Substituir valores ausentes

print("\n--- PASSO 2: Substituindo valores ausentes ---")

# Substitui NA em Vendas pela mediana e Despesas pela média
df["Vendas"].fillna(df["Vendas"].median(), inplace=True)
df["Despesas"].fillna(df["Despesas"].mean(), inplace=True)

print("\nDados após substituição:")
print(df)


# PASSO 3: Agrupar por Região e Mês

print("\n--- PASSO 3: Agrupando por Região e Mês ---")

# Agrupa e calcula soma de vendas e média de despesas
agrupado = df.groupby(["Região", "Mês"]).agg({
    "Vendas": "sum",
    "Despesas": "mean"
}).reset_index()  # reset_index() para transformar o GroupBy em DataFrame

print("\nAgrupamento (Soma de Vendas e Média de Despesas):")
print(agrupado)


# PASSO 4: Combinar horizontalmente Vendas e Despesas

print("\n--- PASSO 4: Combinando colunas Vendas e Despesas ---")

# Converte colunas para arrays numpy e combina
vendas_array = df["Vendas"].values.reshape(-1, 1)
despesas_array = df["Despesas"].values.reshape(-1, 1)
combinado = np.hstack((vendas_array, despesas_array))

print("\nCombinação horizontal (Vendas + Despesas):")
print(combinado)


# PASSO 5: Sumário estatístico

print("\n--- PASSO 5: Sumário estatístico ---")

# Calcula média, mediana e desvio padrão
sumario = df[["Vendas", "Despesas"]].agg(["mean", "median", "std"])

print("\nEstatísticas das colunas numéricas:")
print(sumario)

