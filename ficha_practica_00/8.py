n=0
total_minutos= 0
total_segundos=0
total_horas=0
while n < 5:
    n += 1  # Incrementa n a cada iteração
    total_minutos += int(input(f"Introduza os minutos da música {n}: ")) 
    total_segundos += int(input(f"Introduza os segundos da música {n}: "))

if total_minutos>59:
    total_horas+= total_minutos//60
    total_minutos=total_minutos%60

if total_segundos>59:
    total_minutos+= (total_segundos//60)
    total_segundos=(total_segundos%60)

print("A duração da playlist é:",total_horas,"horas", total_minutos, "minutos", total_segundos,"segundos")