import math

def primo(n):
    if n <= 1:
        return False  
    if n == 2:
        return True   


    
    limite = int(math.sqrt(n)) + 1
    print(limite)
    for i in range(3, limite, 2): 
        print(i)
        if n % i == 0:
            return False  

    return True 


numero = int(input("Digite um número: "))
if primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")