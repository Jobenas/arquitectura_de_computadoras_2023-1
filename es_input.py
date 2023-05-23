import time

if __name__ == '__main__':
    tiempos_registro = list()
    inicio = time.perf_counter()
    # recepcion de data (Operacion E/S)
    num_flag = False

    while not num_flag:
        inicio_registro = time.perf_counter()
        num = input("Ingrese un numero: ")
        fin_registro = time.perf_counter()

        tiempos_registro.append(fin_registro - inicio_registro)
        try:
            num_val = float(num)
            num_flag = True
        except ValueError:
            pass

    # Procesamiento
    resultado = num_val ** 2
    fin = time.perf_counter()
    # Operacion de salida
    print(f"El valor ingresado fue {num_val} y el resultado al cuadrado es {resultado}")
    print(f"El tiempo total de ejecucion fue {fin - inicio} segundos")
    print(tiempos_registro)
    