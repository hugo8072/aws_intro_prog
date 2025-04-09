stack = []

n = 0
while n < 3:
    num = int(input("Introduza o número: "))
   
    if len(stack) == 0 or num > stack[-1]:
        stack.append(num)  
    else:
        stack.insert(0, num)  
    
    n += 1

order = int(input("Introduza zero para ordem crescente ou 1 para ordem decrescente"))

if order ==0:
    print(stack)
else:
    stack.reverse()
    print(stack)