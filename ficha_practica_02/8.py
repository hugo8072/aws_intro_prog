numero = int(input("Introduza um número: "))
soma=0
n=0
while numero != -1:
    print(numero)
    soma+= numero
    n+=1
    numero = int(input("Introduza um número: "))

print("Fim do programa. a media é: ", soma/n)