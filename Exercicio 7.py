'''
EXERCICIO

    faça uma funcao vira_5(fila) que recebe uma fila, retira o primeiro
    elemento do começo da fila e coloca ele de volta, no fim da fila.
    Depois faz isso de novo, pegando o novo primeiro elemento da fila
    e colocando no final...
    Fazendo 5 vezes no total.

    Ex:
    fila = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    depois de vira_5(fila), a fila será [6, 7, 8, 9, 1, 2, 3, 4, 5]

    Utilize as funçoes enfileirar e desenfileirar implementadas anteriormente
'''


def desenfileirar(fila):
    elemento = fila[0]
    fila.pop(0)
    return elemento


def enfileirar(fila, elemento):
    fila.append(elemento)
    return fila


def vira_5(fila):
    for i in range(5):
        elemento = fila[0]
        desenfileirar(fila)
        enfileirar(fila, elemento)
    return fila


fila10 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(vira_5(fila10))
