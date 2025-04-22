matriz = []

x = 0
y = 0
soma = 0

while x < 3:
    linha = []  
    while y < 3:
        numero = int(input(f"Introduza um número na matriz[{x}][{y}]: "))
        linha.append(numero)
        y += 1
    matriz.append(linha)
    y = 0
    x += 1


print("A matriz é:")
for linha in matriz:
    print(linha)