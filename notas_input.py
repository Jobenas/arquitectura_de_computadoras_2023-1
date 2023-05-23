import time

def registra_numero(pista: str) -> float:
    num_flag = False

    while not num_flag:
        num = input(pista)
        
        try:
            num_val = float(num)
            num_flag = True
        except ValueError:
            pass
    
    return num_val
 

if __name__ == "__main__":
    inicio_total = time.perf_counter()

    labs = list()
    num_labs = 14
    inicio_es = time.perf_counter()
    for i in range(num_labs):
        lab = registra_numero(f"Por favor ingrese nota del lab {i + 1}: ")
        labs.append(lab)

    e1 = registra_numero(f"Por favor ingrese la nota del examen 1: ")
    e2 = registra_numero(f"Por favor ingrese la nota del examen 2: ")    
    fin_es = time.perf_counter()

    inicio_cpu = time.perf_counter()
    nota_lab = sum(labs) / len(labs)
    nota_final = ((5 * nota_lab) + (2.5 * e1) + (2.5 * e2)) / 10.0
    fin_cpu = time.perf_counter()

    fin_total = time.perf_counter()

    print(f"Nota finaal: {nota_final}")
    print(f"tiempo total de ejecucion: {fin_total - inicio_total} segundos")
    print(f"tiempo total de operaciones E/S: {fin_es - inicio_es} segundos")
    print(f"tiempo total de procesamiento: {fin_cpu - inicio_cpu} segundos")
