import time
from threading import Thread

resultados = list()

def potencia(n: int, div: int = 1) -> int:
    global resultados
    res = 1

    rango = n // div

    for _ in range(rango):
        res *= n

    resultados.append(res)


if __name__ == "__main__":
    t1 = Thread(target=potencia, args=(100_000, 2))
    t2 = Thread(target=potencia, args=(100_000, 2))

    inicio = time.perf_counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    resultado = resultados[0] * resultados[1]
    fin = time.perf_counter()

    print(f"Tiempo de ejecución: {fin - inicio} segundos")