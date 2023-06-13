import time
from threading import Thread

CUENTA = 50_000_000

def cuenta(n, id):
    while n > 0:
        n -= 1


if __name__ == "__main__":
    t1 = Thread(target=cuenta, args=(CUENTA // 2, 1))
    t2 = Thread(target=cuenta, args=(CUENTA // 2, 2))

    inicio = time.perf_counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion {fin - inicio} segundos")