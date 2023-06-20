import time

def potencia(n: int, div: int = 1) -> int:
    res = 1

    rango = n // div

    for _ in range(rango):
        res *= n

    return res

if __name__ == "__main__":
    inicio = time.perf_counter()
    resultado = potencia(100_000)
    fin = time.perf_counter()

    print(f"Tiempo de ejecución: {fin - inicio} segundos")
