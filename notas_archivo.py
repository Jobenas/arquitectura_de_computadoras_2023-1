import time

if __name__ == '__main__':
    inicio_total = time.perf_counter()

    inicio_es = time.perf_counter()
    with open("notas.csv", "r") as f:
        contenido = f.read()
    fin_es = time.perf_counter()

    inicio_cpu = time.perf_counter()
    filas = contenido.split("\n")

    notas = list()
    for i in range(1, len(filas)):
        fila = filas[i]
        valores = fila.split(",")
        nums = list()
        for valor in valores:
            nums.append(float(valor))

        notas.append(nums)
    
    notas_finales = list()

    for nota in notas:
        nl = sum(nota[1:15]) / len(nota[1:15])
        e1 = nota[15]
        e2 = nota[16]

        nf = ((5 * nl) + (2.5 * e1) + (2.5 * e2)) / 10
        notas_finales.append([nota[0], nf])
    fin_cpu = time.perf_counter()
    fin_total = time.perf_counter()

    print(notas_finales)
    print(f"Tiempo total de ejecucion: {fin_total - inicio_total} segundos")
    print(f"Tiempo total de operaciones E/S: {fin_es - inicio_es} segundos")
    print(f"Tiempo total de procesamiento: {fin_cpu - inicio_cpu} segundos")
    
    