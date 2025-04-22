array1 = []
array2 = []
matriz = []

# Preencher array1
for i in range(10):
    numero = int(input(f"Introduza um número para o array1 na posição {i}: "))
    array1.append(numero)

# Preencher array2
for i in range(10):
    numero = int(input(f"Introduza um número para o array2 na posição {i}: "))
    array2.append(numero)

# Criar matriz 10x2
for i in range(10):
    linha = [array1[i], array2[i]]
    matriz.append(linha)

# Mostrar matriz
print("A matriz 10x2 é:")
for linha in matriz:
    print(linha)
