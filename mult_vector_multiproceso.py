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


if __name__ == "__main__":
    mat_M = np.random.randint(100, size=(M, N))
    vector_A = np.random.randint(100, size=(N, ))

    inicio = time.perf_counter()
    args = zip(mat_M, repeat(vector_A))
    p = Pool(processes=cpu_count())
    resultado = p.starmap(mult_vector_vector, args)
    p.close()
    p.join()
    fin = time.perf_counter()

    print(f"Tiempo de ejecución: {fin - inicio:.3f} segundos")