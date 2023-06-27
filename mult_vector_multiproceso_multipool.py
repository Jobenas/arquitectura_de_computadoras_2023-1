import time
import numpy as np
from itertools import repeat
from multiprocessing import Pool, cpu_count

M = 5000
N = 5000

def mult_vector_vector(x, y):
    suma = 0

    for i in range(len(x)):
        suma += x[i] * y[i]
    
    return suma


def main(mat_M, vector_A, pool_size):
    p = Pool(processes=pool_size)
    args = zip(mat_M, repeat(vector_A))
    resultado = p.starmap(mult_vector_vector, args)
    p.close()
    p.join()

    return resultado


if __name__ == "__main__":
    mat_M = np.random.randint(100, size=(M, N))
    vector_A = np.random.randint(100, size=(N, ))

    pool_size = [2, 4, 8, 16, 32]
    tiempos = list()

    for size in pool_size:
        tiempos_pool = list()
        for i in range(10):
            print(f"Corrida {i + 1} de pool size: {size}")
            inicio = time.perf_counter()
            main(mat_M, vector_A, size)    
            fin = time.perf_counter()
            tiempos_pool.append(fin - inicio)
        tiempo_prom = sum(tiempos_pool) / len(tiempos_pool)
        tiempos.append([size, tiempo_prom])

    print("Tiempos de ejecucion para diferentes tamaños de pool:")
    for item in tiempos:
        print(f"Pool size: {item[0]}, tiempo: {item[1]}")