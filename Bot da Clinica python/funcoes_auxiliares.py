def escolher(pergunta, opcoes): # Definindo a resposta do usuario, se for "sim", aplicar o codigo abaixo, caso contrario retornar "None" e finalizar o codigo
    if input((pergunta + " (sim/nao): ")).lower() != "sim":
         return None

    print("\nOpções disponíveis:") # Mostrando as opções na tela
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i} - {opcao}")
                
    escolha = input("Digite o número da opção desejada: ") # Entrada da opção escolhida pelo usuario
    return opcoes[int(escolha)-1] if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes) else None # Programa analisa a resposta, se estiver dentro dos parametros "1.2.3" executa o codigo.