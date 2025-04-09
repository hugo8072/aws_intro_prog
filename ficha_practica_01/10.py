first_num = int(input("Insira o primeiroo número:"))
second_num = int(input("Insira segundo número:"))

operador = (input("Insira o operador:"))
if operador in "/ + - * ":
    resultado = eval(f"{first_num} {operador} {second_num}")
    print("O resultado é:", resultado)
else:
    print("Operador inválido")    


