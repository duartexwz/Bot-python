from unidecode import unidecode
import random
from datetime import date, timedelta
import json
import os

#============================================CALCULAR IDADE============================================#
def calcular_idade(idade): # Definindo a função para calcular a idade
    dia, mes, ano = map(int, idade.split('/')) # Dividindo a data de nascimento em dia, mes e ano
    nascimento = date(ano, mes, dia) # Criando a data de nascimento
    hoje = date.today() # Pegando a data de hoje

    idade = hoje.year - nascimento.year
    if (hoje.month, hoje.day) < (nascimento.month, nascimento.day):
        idade -= 1
    return idade


#============================================FUNÇÃO PARA AGENDAR CONSULTA============================================#
def agendar_consulta(): # Definindo a função para agendar consulta
        print("\nÓtimo, preencha algumas informações para mim.")      #pedindo o nome do cliente
        nome = input("\nDigite seu nome completo: ")                  # Pedindo as informações do usuario para marcar a consulta
        idade = input("\nDigite sua data de nascimento (dd/mm/aaaa): ") # Pedindo a idade do usuario
        data_nascimento = calcular_idade(idade)                      # Calculando a idade do usuario
        num = input("\nInforme seu número de telefone: ")             # Pedindo o número de telefone do usuario


    # Definindo o menu de opções de consulta
        print("""\n1. Avaliação Geral. 
2. Limpeza/Profilaxia.
3. Urgência ou dor.
4. Outros.""")

        consulta = input("\nEscolha uma das opções de consulta: ") # Definindo a consulta

        consulta_normalizada = unidecode(consulta.strip().lower()) # Normalizando a escolha do usuario


        escolha_consultas = {
            "1": "Avaliação Geral",
            "2": "Limpeza/Profilaxia",
            "3": "Urgência ou dor",          # Definindo o dicionario para as consultas
            "4": "Outros",
            "avaliacao geral": "Avaliação Geral",
            "limpeza/profilaxia": "Limpeza/Profilaxia",
            "urgencia ou dor": "Urgência ou dor",
            "outros": "Outros"
        }

        if consulta_normalizada in escolha_consultas:
            print(f"\nVocê escolheu: {escolha_consultas[consulta_normalizada]}, vamos prosseguir com o agendamento.")#verificando se a escolha do usuario é valida e mostrando a mensagem de confirmacao
        else:
            print("\nOpção inválida. Por favor, tente novamente.")#mostrando a mensagem de erro caso a escolha seja invalida
            return 


#============================================ESCOLHER DATA============================================#
        hoje = date.today() # Definindo a data de hoje

        datas_disponiveis = [hoje + timedelta(days=i) for i in range(1, 31)] # Definindo as datas disponiveis para agendamento (próximos 30 dias)

        data_sorteada = random.sample(datas_disponiveis, 3)# Sorteando uma data aleatória das datas disponíveis

        print(f"\n Datas disponíveis para esse atendimento são:")
        for i, data in enumerate(data_sorteada, start=1):  #mostrando as datas disponíveis para o usuario
            print(f"{i}. {data.strftime('%d/%m/%Y')}")#mostrando a data no formato dia/mes/ano

        escolha_data = input("\nEscolha uma das datas acima (1, 2 ou 3): ")
        
         # Definindo a escolha do usuario para a data

        escolha_data_normalizada = unidecode(escolha_data.strip().lower()) # Normalizando a escolha do usuario
        #definindo o dicionario para as datas sorteadas

        datas_dict = {
            "1": data_sorteada[0],
            "2": data_sorteada[1],
            "3": data_sorteada[2]
        }   


        #verificando se a escolha do usuario é valida e mostrando a mensagem de confirmacao
        if escolha_data_normalizada in datas_dict:
            data_selecionada = datas_dict[escolha_data_normalizada]
            print(f"\nVocê escolheu a data: {data_selecionada.strftime('%d/%m/%Y')}, agora escolha um horário.")
        else:
            print("\nOpção inválida. Por favor, tente novamente.")
            return
        
#============================================ESCOLHER HORÁRIO============================================#

        manha = ["08:00", "09:00", "10:00", "11:00"] # Definindo os horários disponíveis pela manhã

        tarde = ["13:00", "14:00", "15:00", "16:00"] # Definindo os horários disponíveis pela tarde

        horarios_disponiveis = manha + tarde # Juntando os horários disponíveis

        horarios_sorteados = random.sample(horarios_disponiveis, 3) # Sorteando três horários aleatórios dos horários disponíveis

        print(f"\nOs horários disponíveis para esse atendimento são:") # Mostrando os horários disponíveis para o usuario
        for i, horario in enumerate(horarios_sorteados, start=1):
            print(f"{i}. {horario}")
        escolha_horario = input("\nEscolha um dos horários acima (1, 2 ou 3): ") # Definindo a escolha do usuario para o horario

        escolha_horario_normalizada = unidecode(escolha_horario.strip().lower()) # Normalizando a escolha do usuario

        #definindo o dicionario para os horarios sorteados
        horarios_dict = {
            "1": horarios_sorteados[0],
            "2": horarios_sorteados[1],
            "3": horarios_sorteados[2]
        }

#========================================CONFIRMANDO O AGENDAMENTO=============================================#
        #verificando se a escolha do usuario é valida e mostrando a mensagem de confirmacao
        if escolha_horario_normalizada in horarios_dict:
            horario_selecionado = horarios_dict[escolha_horario_normalizada]
            print(f"\nConsulta agendada com sucesso!\nNome: {nome}\nIdade: {data_nascimento}\nTelefone: {num}\nTipo de Consulta: {escolha_consultas[consulta_normalizada]}\nData: {data_selecionada.strftime('%d/%m/%Y')}\nHorário: {horario_selecionado}\n")
        else:
            print("\nOpção inválida. Por favor, tente novamente.")
            return
#========================================ARMAZENAR AS CONSULTAS MARCADAS=============================================#

def carregar_agendamentos(arquivo='agendamento.json'): # Definindo a função para carregar os agendamentos
    try:
        with open('agendamento.json', 'r') as file: # Abrindo o arquivo json
            return json.load(file) # Carregando os agendamentos
    except (FileNotFoundError, json.JSONDecodeError, UnicodeDecodeError):# Tratando possíveis erros
        return [] # Retornando uma lista vazia se o arquivo não existir

def salvar_agendamento(agendamento, arquivo='agendamento.json'): # Definindo a função para salvar o agendamento
    with open(arquivo, 'w') as file: # Abrindo o arquivo json
        json.dump(agendamento, file, indent=4) # Salvando os agendamentos no arquivo json

def armazenar_agendamento(nome, idade, num, tipo_consulta, data_selecionada, horario_selecionado): # Definindo a função para armazenar o agendamento
    agendamentos = carregar_agendamentos() # Carregando os agendamentos existentes

    novo_agendamento = { # Criando um novo agendamento
        "nome": nome,
        "idade": idade,
        "telefone": num,
        "tipo_consulta": tipo_consulta,
        "data": data_selecionada.strftime('%d/%m/%Y'),
        "horario": horario_selecionado
    }

    agendamentos.append(novo_agendamento) # Adicionando o novo agendamento à lista

    salvar_agendamento(agendamentos) # Salvando os agendamentos atualizados
#========================================LOOP SIMPLES DE ESTADOS PARA TESTE=============================================#
if __name__ == "__main__":
    agendar_consulta() # Chamando a função para agendar consulta