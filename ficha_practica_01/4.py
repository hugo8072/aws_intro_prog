pos_points = {
  1: 10,
  2 : 8,
  3: 6,
  4: 5,
  5: 4,
  6: 3,
  7: 2,
  8: 1,
}

posiçao = int(input("Introduza a posição:"))
if posiçao>8:
    print  ("Nao ganhou pontos")
else:    
    print("pontos:", pos_points[posiçao])