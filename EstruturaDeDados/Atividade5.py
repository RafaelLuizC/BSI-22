import numpy as np

matriz = np.zeros((5, 5)) #Cria uma matriz 5x5 com todos os valores 0

for i in range(len(matriz)): #Percorre as colunas da matriz
    for y in range(len(matriz)):
        #Altera os valores para os previamente definidos na atividade.
        if i == y:
                matriz[i, y] = 3*i**2 
        elif i < y: 
                matriz[i, y] = (2*i) + (7*y)
        elif i > y:
                matriz[i, y] = (4*i**3) + (5*y**2)

def printmatriz(): 
    for lista in matriz:
        for elemento in lista:
            print(elemento, end=' ')
        print()

printmatriz()
