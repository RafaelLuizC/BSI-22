import numpy as np

vetor = np.array([])


def Verificador(numero, vetor):
    if numero in vetor:
        return False
    else:
        return True

while len(vetor) < 5:
    valorAdicionado = float(input("Digite um número: "))
    if Verificador(valorAdicionado, vetor) == True:
        vetor = np.append(vetor, valorAdicionado)
    else:
        print("Valor já inserido") 
        continue

print (vetor)