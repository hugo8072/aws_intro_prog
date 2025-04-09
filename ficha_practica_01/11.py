current = int(input("Introduza o saldo médio:"))
movement = int(input("Introduza o valor a movimentar"))

if (current + movement) > 0:
    print("Saldo actual:", current + movement)
else:
    print("Saldo insuficiente. Com esta operaçao ficaria a :", current + movement,"euros")    