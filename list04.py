"""
Escribir un programa que pregunte al usuario los números ganadores de la 
lotería primitiva, los almacene en una lista y los muestre por pantalla 
ordenados de menor a mayor.
"""

lottery_num = []

for i in range(6):
  num = int(input('Enter a winner num: '))
  lottery_num.append(num)
  
lottery_num.sort()
print('Winners numbes ->' ,lottery_num)