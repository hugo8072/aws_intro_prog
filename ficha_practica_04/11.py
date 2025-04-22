matriz = []

x = 0
y = 0
maior = -10000000000000000000000
menor = 10000000000000000000000

while x < 5:
    linha = []  
    while y < 5:
        numero = int(input(f"Introduza um número na matriz[{x}][{y}]: "))
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        linha.append(numero)
        y += 1
    matriz.append(linha)
    y = 0
    x += 1


print("A matriz é:")
for linha in matriz:
    print(linha)

print("O maior número é:", maior)
print("O menor número é:", menor)    