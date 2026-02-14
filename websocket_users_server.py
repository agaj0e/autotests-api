import asyncio

import websockets
from websockets import ServerConnection


async def mess(websocket:ServerConnection):
    async for message in websocket:
        print(f'Получено сообщение: {message}')
        for i in range(1, 6):
            response = f"{i} Сообщение пользователя: {message}"
            await websocket.send(response)
            print(f"Отправлено: {response}")


async def main():
    server = await websockets.serve(mess,"localhost", 8765)
    print("Websocket сервер запущен на адресе ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())