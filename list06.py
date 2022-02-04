"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado 
en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa 
debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

subjetcs = ["Maths", "Physics", "Chemistry", "History", "Language"]
notes = []

# Este for lo uso para guardar las asignaturas aprobadas (las guardo en una nueva)
for s in subjetcs:
  note = int(input(f'What grade did you in {s}: '))
  if note >= 7: # +7 para aprobar
    notes.append(s)

# Este for elimino las notas aprobadas de la lista original (subjects)
for n in notes:
  subjetcs.remove(n)

print('You have to repeat ->',str(subjetcs))