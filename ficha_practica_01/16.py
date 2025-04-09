first_number = int(input("Insira o valor:"))


notes = [5,10,20,50,100,200,500]
n=0

for n in notes:
    print ("Número de notas de",n,"igual a:",first_number//n)
    