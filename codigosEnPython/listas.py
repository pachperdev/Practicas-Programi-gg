**Suma **(+) Concatena dos o más listas:
a=[1,2]
b=[3,4]
a + b --> [1,2,3,4]
**Multiplicación **(*) Repite la misma lista:
a=[1,2]
a * 2 —> [1,2,1,2]
Añadir elemento al final de la lista:
a=[1]
a.append(2)=[1,2]
Eliminar elemento al final de la lista:
a=[1,2]
b=a.pop()
a=[1]
**Eliminar elemento **dado un indice:
a=[1,2]
b=a.pop(1)
a=[2]
Ordenar lista de menor a mayor, esto modifica la lista inicial
a=[3,8,1]
a.sort() —> [1,3,8]
Ordenar lista de menor a mayor, esto NO modifica la lista inicial
a=[3,8,1]
a.sorted() —> [1,3,8]
Eliminar elementos de lista Elimina el elemento de la lista dado su indice
a=[1,2,3]
del a[0] —> a[2,3]
Eliminar elementos de lista Elimina el elemento de la lista dado su valor
a=[0, 2, 4, 6, 8]
a.remove(6)
a=[0, 2, 4, 8]
**Range **creacion de listas en un rango determinado
a=(list(range(0,10,2))) -->crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
a=[0,2,4,6,8]
Tamaño lista len Devuelve el valor del tamaño de la lista:
a=[0,2,4,6,8]
len(a)=5




Estructuras de Datos con Python 🐉 - Listas
.
Las estructuras de datos estándar que incorpora Python son: list, tuple, dict, y set.
.
La estructura de la lista es la siguiente:

mi_lista = [1, 2, 'chocolate', 'vainilla', TRUE]
.
En estas clases veremos el uso de las listas las cuales pueden aplicar diferentes métodos para aumentar su funcionalidad. Los métodos son:
.
append(). Agrega un elemento al final de la lista.

list.append(item)
clear(). Quita todos los elementos de la lista.

list.clear()
copy(). Regresa (copia), los elementos de la lista.

new_list = list.copy()
count(). Regresa el número de veces que un elemento aparece en la lista.

list.count(element)
extend(). Agrega elementos de un iterable(lista, tupla, string, etc) al final de la lista actual.

list1.extend(iterable)
index() Regresa el índice del primer elemento con el valor espcificado.

list.index(element, start, end)
insert(). Agrega elementos en una posición de índice específica.

list.insert(i, elem)
pop(). Quita elementos de una posición específica y permite agregarlos a otra lista.

list.pop(index)
remove(). Elimina el primer elemento que encuentra en la lista con el valor dado. Regresa None.

list.remove(element)
reverse(). Invierte el orden de la lista. No toma argumentos.

list.reverse()
sort(). Ordena la lista de forma ascendente o descendente(reverse = True). No retorna valores.

list.sort(key=..., reverse=...)