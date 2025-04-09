first_quarter = 0
second_quarter = 0
third_quarter = 0
fourth_quarter = 0


num=0

while num != -1:
    num = int(input("Introduza um número: "))
    if num >= 0 and num <= 25:
        first_quarter += 1
    elif num > 25 and num <= 50:
        second_quarter += 1
    elif num > 50 and num <= 75:
        third_quarter += 1
    elif num > 75 and num <= 100:
        fourth_quarter += 1 


print("1º Quadrante: ", first_quarter)
print("2º Quadrante: ", second_quarter)
print("3º Quadrante: ", third_quarter)
print("4º Quadrante: ", fourth_quarter)
print("Fim do programa")
