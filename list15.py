"""
Eliminar los elementos duplicados de una lista

Debe haber mil formas de hacerlo, a mi se me ocurrió (de manera rápida) la siguiente.
Si tienes una idea mejor, o mas fácil, o simplemente otra idea, puedes dejármela a 
través de mis redes sociales que aparecen en mi inicio (:
"""

# Convertimos la lista original en un set. Sabiendo que estos, eliminan los elementos duplicados

original_list = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10]

set_list = set(original_list)
print(set_list)

# Volvemos a convertir el set en una lista
original_list = list(set_list)
print(original_list)
