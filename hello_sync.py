import time

def count(id: int):
    print(f"{id}: Uno")
    time.sleep(1)
    print(f"{id}: Dos")


def main():
    for idx in range(1, 4):
        count(idx)

if __name__ == "__main__":
    inicio = time.perf_counter()
    main()
    fin = time.perf_counter()

    print(f"Tiempo total de ejecucion: {fin - inicio} segundos")
