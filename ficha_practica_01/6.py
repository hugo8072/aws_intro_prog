first_num = int(input("Insira o primeiro número:"))
second_num= int(input("Insira o segundo número:"))

if first_num>second_num:
    biggest=first_num
    smallest=second_num
elif second_num>first_num:
    biggest=second_num
    smallest=first_num
else: 
    print("os numeros sao iguais")        

print ("menor numero:", smallest , "maior numero:", biggest )    