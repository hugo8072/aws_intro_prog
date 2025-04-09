operadores = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Erro: divisão por zero"
}



def calcular(operador, a, b):
    if operador in operadores:
        return operadores[operador](a, b)
    else:
        return "Operador inválido"
    
travao=0
while(travao!='n'):
        first_number = int(input("Insira o valor:"))
        second_number = int(input("Insira o valor:"))
        op = input("Insira o operador:")
        resultado = calcular(op, first_number, second_number)
        print("Resultado:", resultado)
        travao = input("Pretende continuar? (s/n)")
