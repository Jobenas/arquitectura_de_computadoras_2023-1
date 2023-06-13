import socket
from threading import Thread

SOCK_BUFFER = 1024
num_clientes = 0


def client_handler(conn, client_address):
    global num_clientes
    num_clientes += 1
    print(f"Numero de clientes conectados al servidor actualmente: {num_clientes}")
    print(f"Conexion desde {client_address[0]}")

    try:
        while True:
            data = conn.recv(SOCK_BUFFER)
            if data:
                print(f"Recibi {data.decode('utf-8')}")
                conn.sendall(data)
            else:
                print("No hay mas datos")
                break
    finally:
        print("Cerrando conexion con el cliente")
        num_clientes -= 1
        conn.close()


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 5000)

    print(f"Iniciando servidor {server_address[0]}:{server_address[1]}")

    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()

        t = Thread(target=client_handler, args=(conn, client_address))
        t.start()
