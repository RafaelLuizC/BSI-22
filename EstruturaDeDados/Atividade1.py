import numpy as np

# Lendo os conjuntos de números reais
x = np.array([float(input(f"Digite o {i+1}º número do primeiro conjunto: ")) for i in range(5)])
y = np.array([float(input(f"Digite o {i+1}º número do segundo conjunto: ")) for i in range(5)])

# Calculando o produto escalar
prod_escalar = np.dot(x, y)

# Imprimindo os conjuntos e o produto escalar
print(f"Conjunto 1: {x}")
print(f"Conjunto 2: {y}")
print(f"Produto escalar: {prod_escalar}")
