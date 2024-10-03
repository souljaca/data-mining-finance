from analysis import carrega_dados, calcular_total, detectar_fraudes, calcular_estatisticas

# Função principal que executa o fluxo completo do programa.
def main():
    # Carrega os dados do arquivo CSV chamando a função carrega_dados
    transacoes = carrega_dados()
    
    # Calcula o total das transações
    calcular_total(transacoes)
    
    # Detecta possíveis fraudes nas transações
    detectar_fraudes(transacoes)
    
    # Calcula estatísticas básicas das transações
    calcular_estatisticas(transacoes)

# Chama a função principal para executar o código
if __name__ == "__main__":
    main()  # Inicia o fluxo do programa chamando a função main
