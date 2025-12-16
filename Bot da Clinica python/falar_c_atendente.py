import unidecode

def falar_c_atendente(): # Definindo a função para falar com um atendente
    return "\nVocê será redirecionado para um atendente. Por favor, aguarde...\n"

def verificar_atendente(texto): # Função para verificar se o usuário quer falar com um atendente
    texto_normalizado = unidecode.unidecode(texto.lower())
    palavras_chave = ["atendente", "falar com atendente", "suporte", "ajuda humana", "quero falar com alguém"]
    
    for palavra in palavras_chave: # Verificando se alguma palavra chave está no texto
        if palavra in texto_normalizado:
            return True
    return False


async def redirecionar_para_atendente(atendentes): # Função para redirecionar para atendente
    for atendente in atendentes: #enviar mensagem para todos os atendentes conectados
        await atendente.send_text("Novo cliente deseja falar com um atendente. Por favor, inicie o atendimento.") #notificar atendentes