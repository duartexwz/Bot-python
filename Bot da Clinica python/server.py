from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import falar_c_atendente
from falar_c_atendente import verificar_atendente
import unidecode


app = FastAPI()#criação da aplicação FastAPI

clientes = [] #usuarios conectados
atendentes = [] #atendentes conectados


@app.websocket("/ws/cliente") #rota para o websocket do cliente

async def websocket_cliente(websocket: WebSocket): #função para lidar com o websocket do cliente
    await websocket.accept() #aceitar a conexão do websocket
    clientes.append(websocket) #adicionar o cliente à lista de clientes

    try:
        while True: #loop infinito para receber mensagens do cliente
            mensagem = await websocket.receive_text() #receber a mensagem do cliente
            if verificar_atendente(mensagem): #verificar se o cliente quer falar com um atendente
                await websocket.send_text(f"Blue: {falar_c_atendente()}") #enviar mensagem de redirecionamento
                for atendente in atendentes: #enviar mensagem para todos os atendentes conectados
                    await atendente.send_text("Novo cliente deseja falar com um atendente. Por favor, inicie o atendimento.") #notificar atendentes
            else:
                await websocket.send_text(f"Blue: Desculpe, não entendi sua mensagem. Por favor pode digitar novamente?\n") #responder mensagem padrão
    except WebSocketDisconnect: #tratar a desconexão do websocket
        clientes.remove(websocket) #remover o cliente da lista de clientes


@app.websocket("/ws/atendente") #rota para o websocket do atendente

async def websocket_atendente(websocket: WebSocket): #função para lidar com o websocket do atendente
    await websocket.accept() #aceitar a conexão do websocket
    atendentes.append(websocket) #adicionar o atendente à lista de atendentes
    try:
        while True: #loop infinito para receber mensagens do atendente
            mensagem = await websocket.receive_text() #receber a mensagem do atendente
            for cliente in clientes: #enviar a mensagem para todos os clientes conectados
                await cliente.send_text(f"Atendente: {mensagem}") #enviar a mensagem do atendente para o cliente
    except WebSocketDisconnect: #tratar a desconexão do websocket
        atendentes.remove(websocket) #remover o atendente da lista de atendentes
