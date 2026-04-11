import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
import os

# --- ESTRUTURAS DE DADOS ---
# Listas: Usadas para armazenar objetos mutáveis
# Tuplas: Usadas para registros imutáveis (ex: coordenadas ou chaves de configuração)
# Dicionários: Mapeamento de prioridades e categorias
# Deque: Fila de entrega eficiente (O(1) para inserção/remoção nas pontas)
# DataFrame: Processamento tabular de dados em massa

caminho_csv = "../db/Check_point_1_dados_logistica_RA_final_par.csv"

def carregar_dados(caminho_csv):
    """
    Carrega o CSV e retorna um DataFrame.
    O(N) - Onde N é o número de linhas no arquivo.
    """
    if not os.path.exists(caminho_csv):
        print(f"Erro: Arquivo {"../db/Check_point_1_dados_logistica_RA_final_par.csv"} não encontrado.")
        return None
    return pd.read_csv(caminho_csv)

def calcular_prioridade(row):
    """
    Lógica de priorização humana:
    1. Urgência é o fator principal.
    2. Tempo estimado curto em carga alta urgência = Prioridade Máxima.
    3. Status de pagamento pendente reduz a prioridade (risco financeiro).
    """
    # Dicionário de pesos para urgência (O(1) lookup)
    pesos_urgencia = {"alta": 3, "media": 2, "baixa": 1}
    
    score = pesos_urgencia.get(row['urgencia'], 0) * 10
    
    # Se o tempo for curto, a criticidade aumenta (ex: perecíveis)
    if row['tempo_estimado_horas'] < 12:
        score += 5
        
    # Penalidade para pagamento pendente
    if row['status_pagamento'] != 'ok':
        score -= 10
        
    return score

# --- RECURSÃO ---
def calcular_valor_total_recursivo(valores):
    """
    Exemplo simples de recursão para somar valores.
    Big O: O(N) - Visita cada elemento uma vez.
    """
    if not valores:
        return 0
    # Tupla para desempacotar o primeiro e o resto (imutabilidade)
    primeiro, *resto = valores
    return primeiro + calcular_valor_total_recursivo(resto)

def processar_entregas():
    print("--- Iniciando Sistema de Logística Inteligente ---")
    
    # 1. Carregamento (DataFrame)
    df = carregar_dados(caminho_csv)
    if df is None: return

    # 2. Cálculo de Custos e Prioridades
    # Adicionando coluna de custo total
    df['custo_total'] = df['quantidade'] * df['valor_unitario']
    
    # Aplicando a lógica de prioridade
    df['score_prioridade'] = df.apply(calcular_prioridade, axis=1)

    # 3. Ordenação (Sort)
    # Big O: O(N log N) - Algoritmo Timsort do Python/Pandas
    df_ordenado = df.sort_values(by=['score_prioridade', 'custo_total'], ascending=False)
    
    print("\nTop 5 Cargas Prioritárias:")
    print(df_ordenado[['pedido_id', 'produto', 'cidade_destino', 'score_prioridade']].head())

    # 4. Uso de Tuplas e Listas para processamento individual
    pedidos_lista = []
    for _, row in df_ordenado.iterrows():
        # Criamos uma tupla imutável para representar o 'ticket' de entrega
        ticket = (row['pedido_id'], row['cidade_destino'], row['produto'])
        pedidos_lista.append(ticket)

    # 5. Uso de Deque (Fila de Entrega)
    # Ideal para sistemas de despacho onde a ordem de saída importa
    fila_entrega = deque(pedidos_lista)
    
    print(f"\nTotal de pedidos na fila: {len(fila_entrega)}")
    
    # 6. Demonstração de Recursão
    lista_custos = df['custo_total'].tolist()
    valor_total = calcular_valor_total_recursivo(lista_custos)
    print(f"\nValor total em mercadorias (via recursão): R$ {valor_total:,.2f}")

    # 7. Geração de Gráficos (Matplotlib)
    gerar_visualizacoes(df)

    print("\n--- Processamento Concluído. Gráficos gerados. ---")

def gerar_visualizacoes(df):
    # Gráfico 1: Custo Total por Cidade
    plt.figure(figsize=(10, 6))
    df_city = df.groupby('cidade_destino')['custo_total'].sum().sort_values()
    df_city.plot(kind='barh', color='skyblue')
    plt.title('Valor Total de Carga por Destino')
    plt.xlabel('Valor (R$)')
    plt.ylabel('Cidade')
    plt.tight_layout()
    plt.savefig('grafico_custo_cidade.png')
    print("Salvo: grafico_custo_cidade.png")

    # Gráfico 2: Distribuição de Urgência
    plt.figure(figsize=(8, 8))
    df['urgencia'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['red', 'orange', 'green'])
    plt.title('Distribuição de Urgência dos Pedidos')
    plt.ylabel('')
    plt.savefig('grafico_urgencia.png')
    print("Salvo: grafico_urgencia.png")

if __name__ == "__main__":
    processar_entregas()
