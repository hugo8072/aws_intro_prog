n=1
notas =0
dic_notes = {
   1:0.25,
   2:0.35,
   3:0.4,
}
while n<=3:
   notas += float(input(f"introduza a nota do {n} teste ")*dic_notes[n])
   n+=1




if notas>9.5:
   print("O aluno passou com uma média de :", notas)
else:
   print("O aluno reprovou")
    