inicio = int(input("Introduza o primeiro número: "))
fim  = int(input("Introduza o ultimo número: "))

while inicio <= fim:
    if inicio % 5 == 0:
        print (inicio, "é multiplo de 5")
        
    inicio += 1