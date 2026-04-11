DOCUMENTAÇÃO TÉCNICA
SISTEMA DE PROCESSAMENTO LOGÍSTICO INTELIGENTE

ÍNDICE

1. DESCRIÇÃO DO PROJETO
2. FUNCIONALIDADES
3. TECNOLOGIAS UTILIZADAS
4. ESTRUTURA DO PROJETO
5. GUIA DE USO
6. CARACTERÍSTICAS TÉCNICAS
7. EQUIPE

=====================================================

1.DESCRICAO DO PROJETO

=====================================================
O Sistema de Processamento Logístico Inteligente é uma aplicação desenvolvida 
em Python com o objetivo de analisar e organizar pedidos logísticos com base 
em critérios de prioridade.

O sistema utiliza um arquivo CSV como fonte de dados e realiza o processamento 
automático das informações, incluindo cálculo de custos, definição de prioridade 
e geração de relatórios gráficos.

O projeto simula um fluxo logístico real, considerando fatores como urgência, 
tempo estimado de entrega e status de pagamento.

=====================================================

2.FUNCIONALIDADES

=====================================================
O sistema contempla as seguintes funcionalidades:

   - Carregamento de Dados
        * Leitura de arquivo CSV
        * Estruturação em DataFrame

   - Cálculo de Custos
        * Criação da coluna custo total
        * Baseado em quantidade e valor unitario

   - Priorização de Pedidos
        * Cálculo de score de prioridade baseado em:
             - urgência (alta/media/baixa)
             - tempo estimado de entrega 
             - status de pagamento

   - Ordenação de Dados
        * Ordenação por score de prioridade 
        * Critério secundário: custo total

   - Fila de Processamento
        * Conversão dos pedidos em tuplas
        * Inserção em uma fila

   - Cálculo Recursivo
        * Soma total dos valores de carga utilizando recursão

   - Geração de Gráficos
        * Gráfico de barras (custo por cidade)
        * Gráfico de pizza (distribuição de urgência)

=====================================================

3.TECNOLOGIAS USADAS

=====================================================
   - Python 
   - Pandas
   - Matplotlib
   - Collections.deque
   - OS

=====================================================

4.ESTRUTURA DO PROJETO 

=====================================================
projeto/
   │
   |---cp.py                                      # Arquivo principal
   │
   |---Check_point_1_dados_logistica_RA_final_par.csv   # Base de dados
   │
   |---grafico_custo_cidade.png                  # Gerado pelo sistema
   │
   |---grafico_urgencia.png                      # Gerado pelo sistema
   │
   |--- README.md                                 # Documentação

Estrutura interna do código:

   - carregar_dados()
        * Leitura do CSV

   - calcular_prioridade()
        * Define score de prioridade

   - calcular_valor_total_recursivo()
        * Soma valores recursivamente

   - processar_entregas()
        * Controla fluxo principal

   - gerar_visualizacoes()
        * Criação dos gráficos

=====================================================

5.GUIA DE USO

=====================================================
- PRÉ-REQUISITOS

   Instalar dependências:

   pip install pandas matplotlib

- EXECUÇÃO

   Executar o arquivo principal:

   python cp.py

- PROCESSAMENTO

   O sistema executa automaticamente:

  *Leitura do CSV
     *Cálculo de custo_total
     *Cálculo de prioridade
     *Ordenação dos pedidos

- SAÍDA

   O sistema exibe no terminal:

     *Top 5 cargas prioritárias
     *Total de pedidos na fila
     *Valor total das cargas

- RELATÓRIOS

   São gerados automaticamente:

    *grafico_custo_cidade.png
    *grafico_urgencia.png

=====================================================

6.CARACTERISTICAS TECNICAS

=====================================================
- USO DE DEQUE

   - Estrutura First In, First Out
   - Inserção e remoção eficientes 

- RECURSÃO

   - Função para soma de valores

- PRIORIZAÇÃO

   - Uso de dicionário para pesos de urgência
   - Ajuste por tempo estimado
   - Penalidade por pagamento pendente

- PANDAS

   - Manipulação de dados tabulares
   - Criação de colunas
   - Agrupamento e ordenação

- VISUALIZAÇÃO

   - Gráfico de barras horizontal
   - Gráfico de pizza com porcentagem

=====================================================

7.EQUIPE

=====================================================
- Desenvolvimento Principal:  Giovanni Tarzoni Piccin RM:564014,Enrico gianni nóbrega puttini RM: 561400, Jean Carlos Rodrigues da Silva RM: 566439, Bruno Lobosque Rm:561254

=====================================================
