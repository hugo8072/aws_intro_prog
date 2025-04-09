fim = int(input("Quantos números quer inserir?: "))

n=1
aux=-1

while n <= fim:
    numero = int(input("Introduza um número: "))
    if numero> aux:
        aux = numero
        n+=1
    else:
        print("nao é crescente")
        break

if n == fim+1:
    print("sequencia crescente")        