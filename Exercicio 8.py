def desenfileirar(fila):
    elemento = fila[0]
    fila.pop(0)
    return elemento


def enfileirar(fila, elemento):
    fila.append(elemento)
    return fila


def vira_n(fila, n):
    for i in range(n):
        elemento = fila[0]
        desenfileirar(fila)
        enfileirar(fila, elemento)
    return fila


numeros = [1, 2, 3, 4, 5, 6]
print(vira_n(numeros, 3))