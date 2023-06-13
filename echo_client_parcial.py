import socket

SOCK_BUFFER = 4


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ("localhost", 5000)  # cambiar para usar en otra computadora
    
    print(f"Conectando a {server_address[0]}:{server_address[1]}")

    sock.connect(server_address)

    try:
        msg = "Hola Mundo!"
        sock.sendall(msg.encode("utf-8"))
        amnt_expected = len(msg.encode("utf-8"))
        amnt_recvd = 0
        msg_total_bytes = b''   

        while amnt_recvd < amnt_expected:     
            data = sock.recv(SOCK_BUFFER)
            print(f"Recibi {data}")
            msg_total_bytes += data
            amnt_recvd += len(data)
        mensaje_recibido = msg_total_bytes.decode("utf-8")
        print(f"mensaje total = {mensaje_recibido}")
    finally:
        print("Cerrando conexion")
        sock.close()