'''
EXERCICIO

    Faca a funcao 'desenfileirar(fila)' que tira o elemento do inicio
    da fila e o retorna.

    Ou seja:
    fila = [10, 2, 3]
    desenfileirar(fila)    # retorna 10, e a fila fica com os elementos [2, 3]
'''


def desenfileirar(fila):
    elemento = fila[0]
    fila.pop(0)
    return "Elemento desinfileirado: %.f" % elemento


fila5 = list(range(10))
print(desenfileirar(fila5))