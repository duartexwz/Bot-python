import websockets
import asyncio

async def cliente():
    uri = "ws://127.0.0.1:8000/ws/cliente"
    async with websockets.connect(uri) as websocket:
        print("Conectado ao bot. Digite mensagens:")
        while True:
            msg = input("Você: ")
            await websocket.send(msg)
            resposta = await websocket.recv()
            print(resposta)

asyncio.run(cliente())