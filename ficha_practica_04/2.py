n=0
array = [0]*12
# array = [0,0,0,0,0,0,0,0,0,0,0,0,0]

while (n<12):
    numero = int(input(f"Introduza a comissão para o mês numero[{n+1}]: "))
    array[n] = numero
    n=n+1


n=0
soma_comissoes = 0

while (n<12):
    soma_comissoes += array[n]
    n+=1

print("O total de comissões é: ",soma_comissoes)




