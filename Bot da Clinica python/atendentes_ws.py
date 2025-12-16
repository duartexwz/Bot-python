from fastapi import websocket

ws = websocket.WebSocket()
ws.connect("ws://localhost:8000/ws/atendente")

print("Atendente conectado.")

while True:
    msg = input("Atendente: ")
    ws.send(msg)
