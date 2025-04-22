matriz = []

x = 0
y = 0


while x < 4:
    linha = []  
    while y < 4:
        numero = int(input(f"Introduza um número na matriz[{x}][{y}]: "))
        linha.append(numero)
        y += 1
    matriz.append(linha)
    y = 0
    x += 1

x=0
soma=0

while x < 4:
    soma += matriz[x][x]
    x += 1

print("A soma da diagonal principal é:", soma)
