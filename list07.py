"""
Escribir un programa que almacene el abecedario en una lista, elimine de la 
lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla 
la lista resultante.
"""

import string

# obtengo el abecedario por defecto y lo convierto en una lista
letters = list(string.ascii_lowercase)

# hago un rango del largo de la lista, yendo de a uno
for n in range(len(letters), 1, -1):
  if n % 3 == 0:
    letters.pop(n -1)
    
print(letters)