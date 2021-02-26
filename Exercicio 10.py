'''
EXERCÍCIO

    Faça uma funcao fila_inicial(n) que recebe um numero n
    e retorna uma lista [1, 2, 3, ..., n] (ou seja, uma lista
    dos numeros de 1 até n.
'''


def fila_inicial(n):
    fila = list(range(1, n+1))
    return fila


print(fila_inicial(5))
print(fila_inicial(8))