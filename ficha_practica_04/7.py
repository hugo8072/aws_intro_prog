n=0
array = [0]*10
# array = [0,0,0,0,0,0,0,0,0,0]
maior = -10000000000

while (n<10):
    numero = int(input(f"Introduza um número no Array[{n}]: "))
    array[n] = numero
    if numero % 2 == 0 and numero > maior:
        maior = numero

    n+=1

print("o maior número par é", maior)