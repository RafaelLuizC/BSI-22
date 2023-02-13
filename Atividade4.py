import numpy as np

matriz = np.zeros((5, 5))

def printmatriz():
    for lista in matriz:
        for elemento in lista:
            print(elemento, end=' ')
        print()

for coluna in range(len(matriz)):
    (matriz[coluna][coluna]) = 1

printmatriz()