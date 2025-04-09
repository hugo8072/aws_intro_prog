numero = int(input("quer calcular o factorial de que numero: "))
factorial = 1

while numero>0:
    factorial = factorial * numero
    numero = numero - 1
print("o factorial é:",factorial)