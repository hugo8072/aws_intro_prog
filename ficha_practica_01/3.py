
salary=float(input("Introduza o salário:"))
assert salary >0

if salary<=15000:
    print("Taxa a pagar 20%:", salary*0.2)
elif(salary >15000 and salary<=20000):
    print("Taxa a pagar 30%:", salary*0.3)   
elif(salary >20000 and salary<=25000):
    print("Taxa a pagar 35%:", salary*0.35)
else:
    print("Taxa a pagar 40%:", salary*0.40)
