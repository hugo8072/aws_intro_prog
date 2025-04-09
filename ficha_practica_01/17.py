
dic = {}


salary = int(input("Qual o seu salário?:"))

if salary < 2000:
    print("Nao tem possibilidade de crédito")

elif (salary < 4001):
    print("Tem direito a um crédito de:", 0.2*salary)

elif (salary < 6001):
    print("Tem direito a um crédito de:", 0.3*salary)

else:
    print("Tem direito a um crédito de:", 0.4*salary)
