import socket

SOCK_BUFFER = 1024

def valida_data(cmd: str) -> bool:
    try:
        cmd = int(cmd)
    except ValueError:
        return False

    if 2023001 <= cmd <= 20230040:
        return True
    
    return False


def calcula_nota(fila: list[str]) -> float:
    notas = list()
    for valor in fila:
        notas.append(float(valor))
    
    nl = sum(notas[1:15]) / len(notas[1:15])
    e1 = notas[15]
    e2 = notas[16]

    nf = ((5 * nl) + (2.5 * e1) + (2.5 * e2)) / 10

    return nf

def genera_nota(codigo: str) -> float:
    with open("notas.csv", "r") as f:
        contenido = f.read()
    
    filas = contenido.split("\n")

    for fila in filas:
        fila = fila.split(",")
        if fila[0] == codigo:
            nota_final = calcula_nota(fila)
            return nota_final
    
    return -1.0



if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 5000)
    print(f"Iniciando servidor en IP {server_address[0]}, con puerto {server_address[1]}")

    sock.bind(server_address)

    sock.listen(1)

    while True:
        print("Esperando conexiones...")
        conn, client_address = sock.accept()
        print(f"Conexion desde: {client_address[0]}:{client_address[1]}")

        try:
            while True:
                data = conn.recv(SOCK_BUFFER)

                if data:
                    print(f"Recibido {data.decode('utf-8')}")
                    if valida_data(data.decode("utf-8")):
                        nota = genera_nota(data.decode("utf-8"))
                        codigo_alumno = data.decode("utf-8")
                        conn.sendall(f"Nota final para codigo {codigo_alumno}: {nota}".encode("utf-8"))
                    else:
                        conn.sendall(f"Dato de ingreso invalido".encode("utf-8"))
                else:
                    print("No hay mas datos")
                    break
        except ConnectionResetError:
            print("El cliente ha cerrado la conexion de forma abrupta")
        finally:
            print("El cliente ha cerrado la conexion")
            conn.close()

