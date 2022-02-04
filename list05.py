"""
Escribir un programa que almacene en una lista los números del 1 al 10 y 
los muestre por pantalla en orden inverso separados por comas.
"""

num_list = []

for i in range(0, 11):
  num_list.append(i)
  
print(num_list[::-1])