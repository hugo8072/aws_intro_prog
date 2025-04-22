n=0
array = [0]*10
# array = [0,0,0,0,0,0,0,0,0,0]
sum=0

while (n<10):
    numero = int(input(f"Introduza um número no Array[{n}]: "))
    array[n] = numero
    sum+=numero
    n+=1

print("A média é", sum/n)