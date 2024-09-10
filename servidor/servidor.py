import socket

def start_server():
    # Configuração do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Servidor iniciado e aguardando conexões...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão recebida de {addr}")

        while True:
            message = client_socket.recv(1024).decode()
            if not message:
                break

            print(f"Mensagem recebida: {message}")

            if "olá" in message.lower():
                response = "Olá! Como posso ajudar você hoje?"
            elif "tchau" in message.lower():
                response = "Até mais! Tenha um bom dia!"
            else:
                response = "Desculpe, não entendi sua mensagem."

            client_socket.send(response.encode())

        client_socket.close()

if __name__ == "__main__":
    start_server()
