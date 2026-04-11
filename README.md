DOCUMENTAÇÃO TÉCNICA
SISTEMA DE GERENCIAMENTO DE PEDIDOS LOGÍSTICOS

ÍNDICE

1. DESCRIÇÃO DO PROJETO
2. FUNCIONALIDADES
3. TECNOLOGIAS UTILIZADAS
4. ESTRUTURA DO PROJETO
5. GUIA DE USO
6. RECURSOS DE VALIDAÇÃO
7. CARACTERÍSTICAS TÉCNICAS
8. CONTRIBUIÇÃO

===========================================================================

1. DESCRIÇÃO DP PROJERO
   
===========================================================================

O Sistema de Gerenciamento de Pedidos Logísticos é uma aplicação desenvolvida 
em Python com o objetivo de simular o processamento e despacho de cargas com 
base em níveis de prioridade.

O projeto foi construído com foco no uso de estruturas de dados fundamentais, 
validação de entradas e visualização de dados, proporcionando uma abordagem 
prática para organização logística.

O sistema permite cadastro dinâmico de pedidos, ordenação por urgência, 
processamento automatizado e geração de relatórios gráficos para análise.

===========================================================================

2. FUNCIONALIDADES

===========================================================================

O sistema contém as seguintes funcionalidades:

   - Cadastro de Pedidos
        * Inserção dinâmica via terminal
        * Validação completa dos dados inseridos
        * Garantia de ID único para cada pedido

   - Validação de Dados
        * Verificação de entradas inválidas
        * Aceita apenas letras para destino e produto
        * Garante valores positivos para carga
        * Controle de níveis de urgência válidos

   - Priorização de Pedidos
        * Classificação automática por nível de urgência
        * Sistema de pesos para ordenação:
             - Alta (3)
             - Média (2)
             - Baixa (1)

   - Processamento de Pedidos (Diferencial do Projeto)
        * Uso de recursão para despacho sequencial
        * Simulação de fila logística real
        * Registro completo da ordem de saída

   - Geração de Relatórios
        * Gráfico de barras com valor total por destino
        * Gráfico de pizza com distribuição de urgência
        * Visualização clara para análise de dados

===========================================================================

3. TECNOLOGIAS USADAS

===========================================================================

A seguir estão listadas as principais tecnologias empregadas no desenvolvimento:

   - Python 3
        * Linguagem principal do sistema

   - Pandas
        * Manipulação e estruturação dos dados em DataFrame
        * Base para geração dos relatórios

   - Matplotlib
        * Criação dos gráficos (barras e pizza)

   - Collections.deque
        * Implementação de fila eficiente (FIFO)
        * Utilizada no processamento dos pedidos
    
===========================================================================

4. ESTRUTURA DO PROJETO

===========================================================================

A organização dos arquivos do projeto segue a seguinte estrutura:

   projeto/
   │
   |-- cp.py                        # Arquivo principal com toda a lógica do sistema
   │
   |-- README.md                   # Documentação técnica do projeto
   

Estrutura interna do código:

   - Dados Iniciais
        * Lista de dicionários contendo pedidos pré-cadastrados

   - Função adicionar_pedidos()
        * Responsável pela entrada de novos dados via terminal
        * Contém validações completas de entrada

   - Ordenação de Pedidos
        * Utiliza função sorted() com base em pesos de urgência

   - Fila de Processamento
        * Implementada com deque
        * Armazena pedidos como tuplas imutáveis

   - Função despachar_pedidos()
        * Processamento recursivo da fila
        * Registro da ordem de saída

   - Função gerar_relatorio()
        * Geração de gráficos com base nos dados processados

===========================================================================
