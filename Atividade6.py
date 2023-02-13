import numpy as np

#Cria matriz vazia 3x3
matriz = np.zeros((3,3))

for i in range(3):#Preenche matriz com números digitados pelo usuário
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor da posição [{i}][{j}]: "))

#Soma os valores de cada coluna e armazena no vetor soma_colunas
soma_colunas = np.sum(matriz, axis=0) #axis=0 indica que a soma será feita por coluna

print(soma_colunas) # imprime vetor soma_colunas