from pandas import read_csv
from statistics import mean, stdev

# Esta função carrega os dados de transações de um arquivo CSV.
def carrega_dados():
    # Aqui estamos lendo os dados do arquivo CSV
    dados = read_csv('data/transacoes.csv')
    # Retorna os dados lidos
    return dados

# Esta função calcula o valor total das transações financeiras.
def calcular_total(dados):
    total = 0  # Inicializa o total como zero para começar a soma
    # Percorre cada valor na coluna 'Amount' dos dados
    for valor in dados['Amount']:
        total = total + valor  # Adiciona cada valor ao total
    # Exibe o valor total das transações no console
    print("Valor total das transações:", total)

# Esta função detecta possíveis transações fraudulentas.
def detectar_fraudes(dados):
    suspeitas = []  # Inicializa uma lista para armazenar índices de transações suspeitas
    # Percorre cada linha do DataFrame de transações
    for i in range(len(dados)):
        # Verifica se o valor da transação é maior que R$ 5000
        if dados['Amount'][i] > 5000:
            # Adiciona o índice da transação suspeita à lista
            suspeitas.append(i)
            # Imprime uma mensagem indicando uma possível fraude
            print("Possível transação fraudulenta detectada:", dados['Amount'][i], "na linha", i)
    # Retorna a lista de transações suspeitas
    return suspeitas

# Esta função calcula estatísticas básicas das transações.
def calcular_estatisticas(dados):
    # Calcula a média dos valores das transações
    media = mean(dados['Amount'])
    # Calcula o desvio padrão dos valores das transações
    desvio_padrao = stdev(dados['Amount'])
    # Exibe a média das transações
    print("Média das transações:", media)
    # Exibe o desvio padrão das transações
    print("Desvio padrão das transações:", desvio_padrao)
