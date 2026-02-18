import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address =('localhost', 1488)

server_socket.bind(server_address)

server_socket.listen(10)
print("Сервер запущен и ждет подключений")

messages: list[str] = []
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Пользователь с адресом: {client_address} подключился к серверу")

    message = client_socket.recv(1024).decode()
    print(f"Получено сообщение {message} от {client_address}")

    response = f"Сервер получил {message}"
    messages.append(message)

    client_socket.send('\n'.join(messages).encode())
    client_socket.close()




if __name__ == '__main__':
    server()


