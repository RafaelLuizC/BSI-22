import numpy as np
#Recebendo os valores do usuário
Vetor = np.array([float(input(f"Digite o {i+1}º número do primeiro conjunto: ")) for i in range(15)])

#Criando um novo vetor vazio
NovoVetor = np.array([])

#Percorrendo o vetor e compactando.
for valor in Vetor:
    if valor == 0: #Se o valor for 0, não adiciona no novo vetor.
        pass
    else:
        NovoVetor = np.append(NovoVetor, valor) #O valor é adicionado no novo vetor.

#Imprimindo o novo vetor comprimido
print(NovoVetor)