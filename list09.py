"""
Escribir un programa que pida al usuario una palabra y muestre por 
pantalla el número de veces que contiene cada vocal.
"""

vocals = ['a', 'e', 'i', 'o', 'u']
word = str(input('Enter a word: '))

for v in vocals:
  count = 0
  for w in word:
    if w == v:
      count += 1
  
  print(f'The {v} vocal appear {str(count)} times in the word.')