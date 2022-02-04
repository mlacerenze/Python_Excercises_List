"""
Escriba un programa que permita crear una lista de palabras y que, a 
continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.
"""

list_num = int(input('Enter a list len: '))
names = []

for l in range(list_num):
  name = str(input(f'Enter a name ({l+1}): '))
  names.append(name)
  
search_name = str(input('Enter name to search: '))
times = 0

for n in names:
  if search_name in n:
    times = names.count(search_name)
  
print(f'The name appear in list {times} times.')