##  Solicite al usuario una lista de nombres de participantes (separados por
##  coma). El programa debe asignar aleatoriamente a cada persona un amigo
##  invisible, cumpliendo que nadie se tenga a sí mismo
##  Validaciones:
##      Debe haber al menos 3 participantes.
##      No debe haber nombres duplicados (comparar ignorando mayúsculas y
##      espacios extra).
##  Nota: Los resultados varían en cada ejecución por ser aleatorios,
##  pero ninguna persona debe tenerse a sí misma.

import random

Lista_Nombres = []
Nombre = input("Ingrese el nombre de la persona (para terminar, ingrese 'zzz'): ")
while Nombre != "zzz":
    Lista_Nombres.append(Nombre)
    Nombre = input("Ingrese el nombre de la persona (para terminar, ingrese 'zzz'): ")

random.shuffle(Lista_Nombres)

Tupla_Asignada = []
r = len(Lista_Nombres)
for i in range(r):
    electo1 = Lista_Nombres[i]
    electo2 = Lista_Nombres[(i + 1) % r]
    Tupla_Asignada.append((electo1, electo2))


print("Sorteo:")
for e1, e2 in Tupla_Asignada:
    print(f"{e1} va a regalarle a {e2} .")