import time

def ejecuta_notas() -> dict:
    inicio_total = time.perf_counter()

    inicio_entrada = time.perf_counter()
    with open("notas.csv", "r") as f:
        contenido = f.read()
    fin_entrada = time.perf_counter()

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
    inicio_salida = time.perf_counter()
    print(notas_finales)
    fin_salida = time.perf_counter()
    fin_total = time.perf_counter()

    tiempo_total = fin_total - inicio_total
    tiempo_entrada = fin_entrada - inicio_entrada
    tiempo_cpu = fin_cpu - inicio_cpu
    tiempo_salida = fin_salida - inicio_salida

    tiempo_dict = {
        "tiempo_total": tiempo_total,
        "tiempo_entrada": tiempo_entrada,
        "tiempo_salida": tiempo_salida,
        "tiempo_cpu": tiempo_cpu,
        "tiempo_es": tiempo_entrada + tiempo_salida
    }

    return tiempo_dict


if __name__ == '__main__':
    total_list = list()
    entrada_list = list()
    salida_list = list()
    cpu_list = list()
    es_list = list()

    for _ in range(10):
        res = ejecuta_notas()
        total_list.append(res["tiempo_total"])
        entrada_list.append(res["tiempo_entrada"])
        salida_list.append(res["tiempo_salida"])
        cpu_list.append(res["tiempo_cpu"])
        es_list.append(res["tiempo_es"])

    total_list.sort()
    entrada_list.sort()
    salida_list.sort()
    cpu_list.sort()
    es_list.sort()

    print("*********************************************************")
    print(f"Tiempo medio de ejecucion total: {total_list[len(total_list) // 2]}")
    print(f"Tiempo medio de operaciones de entrada: {entrada_list[len(entrada_list) // 2]}")
    print(f"Tiempo medio de operaciones de salida: {salida_list[len(salida_list) // 2]}")
    print(f"Tiempo medio de operaciones de cpu: {cpu_list[len(cpu_list) // 2]}")
    print(f"Tiempo medio de operaciones de E/S: {es_list[len(es_list) // 2]}")