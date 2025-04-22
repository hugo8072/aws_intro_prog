matriz = []

x = 0
y = 0


while x < 3:
    linha = []  
    while y < 5:
        numero = int(input(f"Introduza um número na matriz[{x}][{y}]: "))
        linha.append(numero)
        y += 1
    matriz.append(linha)
    y = 0
    x += 1


descobrir_ocorrencias = int(input(f"Introduza o numero do qual pretende saber as ocorrencias na matriz: "))


x=0
y=0
soma_ocorrencias = 0
while x < 3:
    linha = []  
    while y < 5:
        if matriz[x][y] == descobrir_ocorrencias:
            soma_ocorrencias += 1
        y += 1
    
    y = 0
    x += 1


print("o numero de ocorrencias é", soma_ocorrencias)