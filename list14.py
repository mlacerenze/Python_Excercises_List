"""
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, pida una palabra y elimine esa palabra de la lista.
"""

list_num = int(input('Enter a list len: '))
names = []

for l in range(list_num):
  name = str(input(f'Enter a name ({l+1}): '))
  names.append(name)
  
print(f'Original List -> {names}')

deleted_name = str(input('Enter name to be deleted: '))

while deleted_name in names:
  names.remove(deleted_name)
else:
  print('Name not found.')    

print(f'Name List -> {names}')