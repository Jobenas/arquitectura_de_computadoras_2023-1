import time
from multiprocessing import Process, Manager

def potencia(n: int, rlist: list[int], div: int = 1):
    global resultados
    res = 1

    rango = n // div

    for _ in range(rango):
        res *= n

    rlist.append(res)


if __name__ == "__main__":
    manager = Manager()
    resultados = manager.list()
    
    p1 = Process(target=potencia, args=(100_000, resultados, 2))
    p2 = Process(target=potencia, args=(100_000, resultados, 2))

    inicio = time.perf_counter()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    resultado = resultados[0] * resultados[1]
    fin = time.perf_counter()

    print(f"Tiempo de ejecución: {fin - inicio} segundos")