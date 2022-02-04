"""
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

Qué es un palíndromo?
  - Son palabras que se leen en igual en un sentido que en otro. (Capicúa)
"""

word = str(input('Enter a word: '))

if word == word[::-1]:
  print('Your word is a palindrome!')
else:
  print('No no, bye.')