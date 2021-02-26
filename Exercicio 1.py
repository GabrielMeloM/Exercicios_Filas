def enfileirar(fila, elemento):
    fila.append(elemento)
    return fila


fila = list(range(10))
enfileirar(fila, 2)
print(fila)