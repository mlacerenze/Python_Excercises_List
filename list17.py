"""
Programa que declare una lista y la vaya llenando de números hasta que 
introduzcamos un número negativo. Entonces se debe imprimir el vector 
(sólo los elementos introducidos).
"""

int_list = []
element = 0

while element >= 0:
    element = int(input('Enter a positive number: '))
    int_list.append(element)
else:
  print('Negative number aren`t valids.')
  
print(f'Positive List -> {int_list}')
