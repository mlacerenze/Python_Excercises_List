"""
Escribir un programa que almacene en una lista los siguientes precios, 
50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
"""

prices = [50, 75, 46, 22, 80, 65, 8]
prices.sort()
lowest = prices[::-1]
print(f'The biggest price is: {prices[-1]} and the lowest price is: {prices[0]}')