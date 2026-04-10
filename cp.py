# 1. DICIONÁRIO (Mapeamento de Pesos de Urgência)
# Útil para transformar texto em valor numérico para ordenação O(1) de acesso
pesos_urgencia = {"alta": 3, "media": 2, "baixa": 1}

# 2. LISTA DE DICIONÁRIOS (Dados extraídos da sua imagem)
dados_brutos = [
    {"id": 1, "destino": "SP", "prod": "Arroz", "urg": "alta", "valor": 500}, # 100 * 5
    {"id": 2, "destino": "RJ", "prod": "Feijao", "urg": "media", "valor": 1200},
    {"id": 3, "destino": "MG", "prod": "Milho", "urg": "baixa", "valor": 600},
    {"id": 4, "destino": "BA", "prod": "Soja", "urg": "alta", "valor": 2100},
    {"id": 5, "destino": "PR", "prod": "Cafe", "urg": "media", "valor": 2500},
]

# 3. ORDENAÇÃO (Requirement)
# Complexidade Timsort: O(n log n)
pedidos_ordenados = sorted(
    dados_brutos, 
    key=lambda x: pesos_urgencia[x['urg']], 
    reverse=True
)

# 4. DEQUE (Fila de Processamento)
# Inserir e remover da fila de pedidos com O(1)
fila_saida = deque()
for pedido in pedidos_ordenados:
    # TUPLA (Imutabilidade): Registra o estado do pedido ao entrar na fila
    registro_imutavel = (pedido['id'], pedido['destino'], pedido['urg'])
    fila_saida.append(pedido)

# 5. RECURSÃO SIMPLES (Processamento da Fila)
historico_final = []

def despachar_pedidos(fila):
    if not fila:
        return
    
    atual = fila.popleft()
    print(f"[DESPACHO] Pedido {atual['id']} - Destino: {atual['destino']} | Prioridade: {atual['urg']}")
    historico_final.append(atual)
    
    despachar_pedidos(fila) # Chamada recursiva

print("--- Início do Processamento de Saídas ---")
despachar_pedidos(fila_saida)

# 6. DATAFRAME E GRÁFICOS
df = pd.DataFrame(historico_final)

def gerar_relatorio(dataframe):
    plt.style.use('ggplot')
    fig, ax = plt.subplots(1, 2, figsize=(14, 5))
    
    # Gráfico 1: Valor por Destino
    dataframe.plot(kind='bar', x='destino', y='valor', ax=ax[0], color='teal')
    ax[0].set_title('Valor Total da Carga por Destino')
    
    # Gráfico 2: Distribuição de Urgência
    dataframe['urg'].value_counts().plot(kind='pie', autopct='%1.1f%%', ax=ax[1])
    ax[1].set_title('Distribuição de Urgência')
    
    plt.tight_layout()
    plt.show()

gerar_relatorio(df)