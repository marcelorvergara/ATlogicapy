#Python test
from functions import *

clear()

mt = []
mt = abrir('CARROS.TXT')

calc = 0
custo_tot = 0

for i in range (1,7):
  print (mt [i][0],mt [i][1],mt [i][2],mt [i][3],mt [i][4])
  valor = (mt [i][1])
  valor = valor.replace("R$","")
  valor = valor.replace("\n","")
  valor = valor.replace(".","")
  valor = valor.replace(",",".")
  valor = float (valor)

  imp = (mt [i][2])
  imp = imp.replace("R$","")
  imp = imp.replace("\n","")
  imp = imp.replace(".","")
  imp = imp.replace(",",".")
  imp = float (imp)
  
  cons = (mt [i][3])
  cons = cons.replace("R$","")
  cons = cons.replace("\n","")
  cons = cons.replace(".","")
  cons = cons.replace(",",".")
  cons = float (cons)
  cons =  round((10000/cons*3.98),2)

  seg = (mt [i][4])
  seg = seg.replace("R$","")
  seg = seg.replace("\n","")
  seg = seg.replace(".","")
  seg = seg.replace(",",".")
  seg = float (seg)

  calc = valor + imp + cons +seg
  print(f"O valor do custo total é", calc)
  print("\t")

  if i == 1:
    custo_tot = calc
    melhor_custo = (mt[i][0])

  if calc < custo_tot:
    custo_tot = calc
    melhor_custo = (mt[i][0])

print("O melhot carro referente ao custo anual é o", melhor_custo)
print ("Com o custo anual de R$", custo_tot)

