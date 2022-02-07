"""
Programa que vaya llenando dos listas de numeros, una 
lista de positivos y otra de negativos. 
Imprimir ambas listas.
"""

positive_list = []
negative_list = []
element = 0 
opt = 's'

while opt == 's':
  element = int(input('Enter a number: '))
  if element >= 0:
    positive_list.append(element)
  else:
    negative_list.append(element)
    
  opt = str(input('Continue?: "s" or "n" -> '))
  if opt == 's':
    continue
  else:
    break
  
print(f'Positive List -> {positive_list} \nNegative List -> {negative_list}')