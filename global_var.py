var = 4


def suma(a, b):
    global var_global
    var_global = "Esta es la verdadera variable global"
    return a + b

def imprime_global():
    global var_global
    print(var_global)


def main():
    res = suma(var, 2)
    var_global = "variable global"
    imprime_global()
    

    print(f"resultado final: {res}")

if __name__ == '__main__':
    main()