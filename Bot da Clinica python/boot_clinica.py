from agendar_consulta import agendar_consulta
from contato_clinica import contato_clinica
from falar_c_atendente import falar_c_atendente
from duvidas import duvidas
import datetime
from unidecode import unidecode


def saudacao(): # Definindo a saudação conforme o horário
    hora_atual = datetime.datetime.now().hour
    if 5 <= hora_atual < 12: #se for entre 5 e 12 retornar "Bom dia!"
        return "Bom dia!"
    elif 12 <= hora_atual < 18: #se for entre 12 e 18 retornar "Boa tarde!"
        return "Boa tarde!"
    else: #se nao for nenhum dos dois, retorna "Boa noite!"
        return "Boa noite!"

#definindo as possiveis saudações do usuario
possiveis_saudações = ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite", "oii", "e ai", "ei", "atendimento", "oi, tudo bem?", "olá, tudo bem?", "ola, tudo bem?"]

#definindo o menu de atendimento
menu = """1. Agendar Consulta.
2. Contato da clínica.
3. Dúvidas Frequentes.
4. Falar com um Atendente."""


#definindo as respostas do bot de acordo com a mensagem do usuario 
respostas = (f"Olá {saudacao()}, Eu sou Blue, o bot de atendimento da Clínica Odonto Silva." "Aqui está seu menu de atendimento⬇️\n")

while True: # Definindo o loop de mensagem do usuario
    mensagem = input("Você: ")
    mensagem_normalizada = unidecode(mensagem.strip().lower())

    if mensagem_normalizada in possiveis_saudações: # Verificando se a mensagem do usuario é uma saudação
        print("Blue:", respostas)
        print(menu)
    else:
        print("Blue: Desculpe, não entendi sua mensagem. Por favor pode digitar novamente?\n")
        
    if mensagem_normalizada in respostas: # Definindo as opções caso o usuario digiti "algumas das palavras chave"
       print("Blue:", respostas[mensagem_normalizada],
       """1. Agendar Consulta.
 2. Contato da clínica.
 3. Dúvidas Frequentes.
 4. Falar com um Atendente.""")

    escolha = input("\nEscolha uma das opções: ").strip() # Definindo a escolha do usuario

    escolha_normalizada = unidecode(escolha.lower()) #normalizadno a escolha do usuario

    if escolha_normalizada in ["1", "agendar consulta"]: #puxando a função de agendar consulta
        agendar_consulta()
    elif escolha_normalizada in ["2", "contato da clinica", "contato da clínica"]: #puxando a função de contato da clinica
        contato_clinica()
    elif escolha_normalizada in ["3", "duvidas frequentes", "dúvidas frequentes"]: #puxando a função de duvidas frequentes
        duvidas()
    elif escolha_normalizada in ["4", "falar com um atendente"]: #puxando a função de falar com atendente
        falar_c_atendente()


#definindo o redirecionamento para as funções conforme a escolha do usuario
    respostas_escolha = {
        "Agendar consulta": agendar_consulta,
        "Contato da clínica": contato_clinica,
        "Dúvidas frequentes": duvidas,
        "Falar com um atendente": falar_c_atendente
    }

    def redirecionar_para_atendente(): # Função para redirecionar para atendente
        print("\nVou te encaminhar para a nossa atendente virtual. Por favor, aguarde um momento...\n")
            