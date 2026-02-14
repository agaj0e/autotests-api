import asyncio
import websockets


async def client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        print(f"Отправка: {message}")

        # Отправляем сообщение серверу
        await websocket.send(message)

        # Получаем 5 ответных сообщений от сервера
        for i in range(5):
            response = await websocket.recv()
            print(f"Ответ от сервера: {response}")


asyncio.run(client())