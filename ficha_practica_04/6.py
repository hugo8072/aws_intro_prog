n=0
array = [0]*10
# array = [0,0,0,0,0,0,0,0,0,0]
sum=0

while (n<10):
    numero = int(input(f"Introduza um número no Array[{n}]: "))
    array[n] = numero
    if numero < array[n-1] and n>0:
        print("O número introduzido é menor que o anterior. Nao esta em ordem crescene")
        break
    n+=1

if n== 10:
    print("Está em ordem crescente")