hour = int(input("Introduza a hora"))
minutes=int(input("Introduza os minutos"))

if hour>12:
    hour-=12

print("A hora em horário de 12 horas é:",hour, "e",minutes,"minutes")