'''
EXERCICIO

    faça uma funcao vira_1(fila) que recebe uma fila, retira o primeiro
    elemento do começo da fila e coloca ele de volta, no fim da fila

    Ex:
    fila = [1, 2, 3, 4, 5]
    se fizermos vira_1(fila), a fila passa a ser [2, 3, 4, 5, 1]

    Utilize as funçoes enfileirar e desenfileirar implementadas anteriormente
'''


def vira_1(fila):
    elemento = fila[0]
    fila.pop(0)
    fila.append(elemento)
    return fila

fila9 = list(range(10))
print(vira_1(fila9))