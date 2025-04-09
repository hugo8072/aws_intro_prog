first_num = int(input("Insira um número:"))
second_num = int(input("Insira um número:"))
third_num = int(input("Insira um número:"))
biggest=0

if first_num>second_num and first_num>third_num:
    biggest=first_num

elif second_num > first_num and second_num> third_num:
    biggest=second_num

else:
    biggest=third_num

print("Maior número:", biggest)            