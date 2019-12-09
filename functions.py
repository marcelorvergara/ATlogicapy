# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
from time import sleep 
  
# define our clear function 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def abrir(local):
  matriz = []
  arq = open (local,'r')
  conteudo = arq.readlines()
  #linhas do arquivo
  l = int(conteudo[0])

  #colunas do arquivo
  c = int(conteudo[1])
  
  p = 2
  i = 0
  while i < l:
    j = 0
    linha = []
    while j < c:
      linha.append(conteudo[p])
      p+=1
      j+=1
    matriz.append(linha)
    i+=1
  #print(matriz)
  arq.close()
  return(matriz)   
