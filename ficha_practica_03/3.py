numero = int(input("Introduza um número "))

tentativa = 0

while tentativa!= numero:
    tentativa = int(input("Introduza o número que quer adivinhar: "))
    if tentativa < numero:
        print("O número é maior")
    elif tentativa > numero:
        print("O número é menor")
    else:
        print("Parabéns, acertou!")