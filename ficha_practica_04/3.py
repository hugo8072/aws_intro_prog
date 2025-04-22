n=0
array = [0]*10
# array = [0,0,0,0,0,0,0,0,0,0]
biggest = -10000000000

while (n<10):
    numero = int(input(f"Introduza um número no Array[{n}]: "))
    array[n] = numero
    if numero > biggest:
        biggest = numero
    n+=1

print("O maior numero é", biggest)