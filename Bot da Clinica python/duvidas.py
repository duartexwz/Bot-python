from datetime import datetime
from funcoes_auxiliares import escolher
from unidecode import unidecode

def saudacao(): # Definindo a saudação conforme o horário
    agora = datetime.now()
    hora = agora.hour


    if 5 <= hora< 12:
        return "Bom dia!" #se a hora for entre 5 e 12, retorna bom dia

    elif 12<= hora < 18:
        return "Boa Tarde!" #se a hora for entre 12 e 18, retorna boa tarde

    else:
        return "Boa Noite!" #se nao for nenhum dos dois, retorna boa noite
     
def duvidas(): # Definindo a função para responder as dúvidas frequentes
    print(saudacao(),"Irei te enviar o nosso menu de duvidas frequêntes, caso sua duvida seja outra, irei te encaminhar para nossa central de atendimento. \n")

    print("""\n1. Quais os tratamentos mais comuns?
2. Quais os benefícios?
3. Quanto tempo leva para ver os resultados?
4. É possível obter resultados permanentes?
5. Quais os riscos?
6. Quais os cuidados pré e pós-tratamento? 
7. A clínica segue as normas de segurança?
8. Nenhuma das anteriores.\n""")

    escolha = input("Escolha qual é a sua dúvida que nós iremos responder.\n") # Definindo a escolha do usuario

    if escolha is not escolha.strip(): # Verificando se a escolha é válida
        print("Não entendi, pode digitar novamente?")
        return
    
    escolha_normalizada = unidecode(escolha.strip().lower()) # Normalizando a escolha do usuario


 # Definindo as respostas para as dúvidas frequentes
    respostas = {
         "quais os tratamentos mais comuns?": """Os tratamentos mais buscados na clínica incluem:

- Limpeza de pele profunda
- Peeling químico
- Microagulhamento
- Botox (toxina botulínica)
- Preenchimento com ácido hialurônico
- Laser para manchas e depilação
- Tratamentos contra acne e melasma

Cada tratamento é recomendado conforme a necessidade individual do paciente.
""",

        "quais os beneficios?": """Os benefícios dos tratamentos estéticos incluem:

- Melhora da aparência da pele
- Controle da oleosidade e acne
- Redução de linhas de expressão
- Clareamento de manchas
- Rejuvenescimento facial 
- Aumento da autoestima
""",

        "quanto tempo leva para ver os resultados?": """O tempo varia conforme o tratamento:

- Botox: 3 a 7 dias
- Preenchimento: imediato
- Microagulhamento: 10 a 20 dias
- Peeling: 1 a 2 semanas
- Laser: 3 a 6 sessões
- Limpeza de pele: imediato
""",

        "e possivel obter resultados permanentes?": """A maioria dos tratamentos não é permanente, mas dura bastante:

- Preenchimento: 6 a 18 meses
- Botox: 3 a 6 meses
- Laser: resultados duradouros com manutenção
""",

        "quais os riscos?": """Os riscos são mínimos quando realizados com profissionais qualificados:

- Vermelhidão
- Sensibilidade
- Pequenos hematomas
- Inchaço leve

Reações sérias são raras.
""",

        "quais os cuidados pre e pos-tratamento?": """Cuidados antes:

- Evitar sol
- Não usar produtos irritantes
- Hidratar a pele

Cuidados depois:

- Usar protetor solar
- Não manipular a área
- Evitar exercícios por 24–48h
- Usar cremes indicados
""",

        "a clinica segue as normas de seguranca?": """Sim! A clínica segue todos os protocolos de biossegurança da ANVISA:

- Ambiente esterilizado
- Profissionais qualificados
- Equipamentos regulamentados
- Uso de EPIs
- Produtos originais
""",
        "nenhuma das anteriores": "Certo, vou te encaminhar para a nossa atendente para te passar mais informações detalhadas.",
    

    }

    opcoes = {
        "quais os tramentos mais comuns": 1,
        "quais os benefícios": 2,
        "quanto tempo leva para ver os resultados": 3,
        "é possível obter resultados permanentes": 4,
        "quais os riscos": 5,
        "quais os cuidados pré e pós-tratamento": 6,
        "a clínica segue as normas de segurança": 7,
        "nenhuma das anteriores.": 8
    }

    if escolha_normalizada not in respostas: # Verificando se a escolha é válida
        print("Não entendi, pode digitar novamente?")
        return
    else:
        print("\n",respostas[escolha_normalizada]) # Mostrando a resposta para a dúvida escolhida pelo usuário


def redirecionar_para_atendente(): # Função para redirecionar para atendente
    print("\nVou te encaminhar para a nossa atendente virtual. Por favor, aguarde um momento...\n")