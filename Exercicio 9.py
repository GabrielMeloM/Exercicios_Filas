def desenfileirar(fila):
    elemento = fila[0]
    fila.pop(0)
    return elemento


def enfileirar(fila, elemento):
    fila.append(elemento)
    return fila


def vira_4_mata_1(fila):
    for i in range(5):
        elemento = fila[0]
        desenfileirar(fila)
        enfileirar(fila, elemento)
    fila.pop(-1)
    return fila


fila12 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(vira_4_mata_1(fila12))
