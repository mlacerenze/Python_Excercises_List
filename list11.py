"""
Escriba un programa que permita crear una lista de palabras. Para ello, 
el programa tiene que pedir un número y luego solicitar ese número de 
palabras para crear la lista. Por último, el programa tiene que escribir la lista.
"""

list_num = int(input('Enter a list len: '))
names = []

for l in range(list_num):
  name = str(input(f'Enter a name ({l+1}): '))
  names.append(name)

print(f'The list of names if -> {names}')