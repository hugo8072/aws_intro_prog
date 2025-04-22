n=0
array = [0]*10
# array = [0,0,0,0,0,0,0,0,0,0]

while (n<10):
    numero = int(input(f"Introduza um número no Array[{n}]: "))
    array[n] = numero
    n+=1


n=0

while (n<10):
    print("Array[",n,"] = ",array[n])
    n+=1




