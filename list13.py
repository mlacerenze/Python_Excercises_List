"""
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.
"""

list_num = int(input('Enter a list len: '))
names = []

for l in range(list_num):
  name = str(input(f'Enter a name ({l+1}): '))
  names.append(name)
  
print(f'Original List -> {names}')

search_name = str(input('Enter name to be replaced: '))
replace_word = str(input('Enter name to replace: '))
count = 0

if search_name in names:
  for n in names:
    if n == search_name:
      names[count] = replace_word 
    count += 1
else:
  print('Name not found.')    

print(f'Name List -> {names}')