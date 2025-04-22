matriz = []

x = 0
y = 0
soma = 0

while x < 5:
    linha = []  
    while y < 5:
        numero = int(input(f"Introduza um número na matriz[{x}][{y}]: "))
        soma += numero
        linha.append(numero)
        y += 1
    matriz.append(linha)
    y = 0
    x += 1

print("A soma é:", soma)
print("A matriz é:")
for linha in matriz:
    print(linha)