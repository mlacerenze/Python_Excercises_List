"""
Crea una lista e inicializala con 5 cadenas de caracteres leídas por 
teclado. Copia los elementos de la lista en otra lista pero en orden 
inverso, y muestra sus elementos por la pantalla.
"""

import copy

len_list = int(input('Enter a len of list: '))
word_list = []
copy_list = []

for i in range(len_list):
  word = str(input(f'Enter a word ({i+1}): '))
  word_list.append(word)

print(word_list)

copy_list = copy.deepcopy(word_list)
print(copy_list[::-1])