'''
# Tipos de dato lista con métodos

# Método .append añade un elemento al final de la lista
array_example1= ['apple', 'Juan', 23]
array_example1.append(68)
print(array_example1)
'''

''''
# Método .extend se utiliza para añadir elementos de una lista a otra lista

array_example2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
array_addNumbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
array_example2.extend(array_addNumbers)
print(array_example2
)
'''

'''
# Método .insert añade x elemento en i posición determinada. Donde especificamos en que lugar de la lista deseamos insertar ese elemento

array_example3 = ['Porsche', 'Bugatti', 'Aston Martin', 'Ferrari']
array_example3.insert(2,'Maserati')
print(array_example3)
'''

'''
# Método .remove como su nombre lo indica, quita o elimina un elemento de la lista donde su valor debe ser especificado, de lo contrario, mostrará un error en pantalla

array_example4 = ['Apple', 'Xiaomi', 'Samsung', 'Huawei']
array_example4.remove('Samsung')
print(array_example4)
'''

'''
# Método .pop elimina un elemento de la lista dada una posición, si no se especifica el indice del elemento a eliminar, remueve el último elemento y lo retorna

array_example5 = ['Juan', 'David', 'Esteban', 'Fernando']
array_example5.pop(1)
print(array_example5)
'''

'''
# Método .clear elimina todos los elementos de una lista 

clear_method = ['Juan', 'David', 'Esteban', 'Fernando']
clear_method.clear()
print(clear_method)
'''

'''
# Método .index Retorna el índice del elemento dentro del arreglo

index_method = ['Smartphone', 'Laptop', 'Computadora']
print(index_method.index('Computadora'))
'''

'''
# Método .count retorna el número de veces que un elemento se encuentra en la lista

count_method = ['Automovil', 'motocicleta', 'Bus', 'Avion', 'motocicleta']
print(count_method.count('motocicleta'))
'''

'''
# Método .sort ordena los elementos de una lista, en orden ascendente o descendente

sort_method = [5, 4, 6, 8, 3]
sort_method.sort()
print(sort_method)

# orden descendente
sort_method = [5, 4, 6, 8, 3]
sort_method.sort(reverse=True)
print(sort_method)
'''

'''
# Método .reverse en pocas palabras, invierte los elementos del arreglo

reverse_method = ['Cali', 'Bogotá', 'Medellín', 'Santander']
reverse_method.reverse()
print(reverse_method)
'''

'''
# Método .copy hace una copia de la lista, creando una variable guardamos esa copia del arreglo

copy_method = [6, 7, 8, 10, 23, 4]
save_numbers = copy_method.copy()
print(save_numbers)
'''

'''
# Listas como pilas, colocar elementos encima de la lista, donde el último elemento ingresado será el primero en eliminarse
# Para ello, utilizamos los métodos .append y .pop
array_stack = ['Mouse', 'Teclado', 'CPU', 'Monitor']

array_stack.append(1500)
array_stack.append(2000)
array_stack.append(900)
array_stack.append(120)

array_stack.pop()
array_stack.pop()
array_stack.pop()

print(array_stack)
'''

'''
# Listas como colas, al contrario de las listas como pilas, en este caso, el primer elemento añadido, será retirado
# Utilizamos la librería collections.deque para implementar una cola

from collections import deque

array_tail = deque([10, 20, 30, 40, 50, 60, 70])

# Luego, añadimos los elementos al final de la lista

array_tail.append(11)
array_tail.append(21)
array_tail.append(31)
array_tail.append(51)
array_tail.append(61)

# Eliminamos los primeros elementos de la lista

array_tail.popleft()
array_tail.popleft()
array_tail.popleft()
array_tail.popleft()
array_tail.popleft()

print(array_tail)
'''

'''
# Comprension de listas

list_comprehension = [2, 4, 2, 4]
list2_comprehension = ["J", "U", "A", "N"]

# Le daremos instrucciones de lo que debe hacer para cada uno de los elementos dentro de la lista 1 y la lista 2

comprehension = [n * num for n in list2_comprehension for num in list_comprehension]

# Lo que hara el programa sera que, multiplique cada elemento de la lista dos con los elementos de la lista 1 respectivamente

print(list_comprehension)
print(comprehension)
'''

'''
# Listas por comprension anidadas, son bastante sencillas de explicar, lo que haremos es crear 3 arreglos, uno vacio y los otros dos con elementos, de allí, anidamos los elementos de los arreglos al del primero

array_container = []
array1_elements = [5, 6, 7]
array2_elements = ["Laptop", "Smartphone", "Computer"]

# Añadimos los elementos al container con el metodo .append

array_container.append(array1_elements)
array_container.append(array2_elements)

print(array_container)
'''

'''
# Instruccion del, funciona similar al metodo .pop pero la diferencia es que la instruccion del necesita de un indice y no de un valor del elemento dentro del arreglo

del_array = [34, 45, 56, 90]
del del_array[2]
print(del_array)

# Incluso, del puede usarse para eliminar variables
del del_array
'''

'''
# Las tuplas son datos tipo secuencia, son inmutables y se caracterizan por tener sus elementos encerrados en parentesis

tuple_example = ("q", "w", "e", "r", "t", "y")
print(tuple_example)

# Tambien podemos crear tuplas vacias o tuplas con un elemento seguido de una coma

empty_tuple = ()
print(empty_tuple)

an_element = 4,
print(an_element)

# Las tuplas permiten consultas sencillas

print(tuple_example[1:4])
'''
'''
# Conjuntos, son una coleccion no ordenada y sin elementos repetidos donde podremos alojar elementos múltiples en ella, se representan con llaves "{}"

data_box = {"c", 32, 94, "tesla", 100, 148, 123, "juan", 6}

print("c" in data_box)
print(24 in data_box)

# Tambien soportan algo similar con la compresion de listas, es decir, comprension de conjuntos

data_box = {n * 2 for n in range(2, 5)}
print(data_box)
'''

'''
# Diccionarios son un tipo de dato que permite almacenar cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones. Estos diccionarios nos permiten además identificar cada elemento por una clave (Key).
# Para definir un diccionario, se encierra el listado de valores entre llaves. Las parejas de clave y valor se separan con comas, y la clave y el valor se separan con dos puntos.

dictionary_example = {
    "smartphone": 250,
    "car": 2000, 
    }
print(dictionary_example)

#Añadir datos

dictionary_example ["laptop"] = 950
print(dictionary_example)


# Eliminar datos 

del dictionary_example["car"]
print(dictionary_example) 

# Convertir a lista

list(dictionary_example)
print(dictionary_example)

# Si se quiere ordenar una insercion, utilizamos sorted(d)

sorted(dictionary_example)
print(dictionary_example)

# Podemos hacer comprension de diccionarios y crear diccionarios de esa manera

dictionary = {n: n**2 for n in (2, 4, 6)}
print(dictionary)
'''

'''
# Iteraciones, podemos definir las iteraciones como la verificacion multiple de una condicion y en caso de que no se cumpla, salimos de la iteracion para realizar otras acciones  
# Comenzamos con el bloque for

for n in range(4):
    print('iteracion: ',n)

# bloque while

m = 0
while (m !=10):
    print('iteracion: ',m)
    m = m + 1

# La funcion zip nos permite a empaquetar elementos iterables

list_1 = [i for i in range(12)]
list_2 = [i+1 for i in range(8)]
list_3 = [i+2 for i in range(8)]

for x,y,z in zip(list_1, list_2, list_3):
    print(x,y,z)

# Iteracion de manera inversa, utilizamos la funcion reversed()

for it in reversed(range(5,10,15)):
    print(it)

# Iterar sobre secuencia ordenada, utilizamos la funcion sorted()

box_array = ['glases', 'eraser', 'pencil', 'ball', 'book', 'notebook', 'money']
for ord in sorted(box_array):   
    print(ord)

# Con la funcion set() eliminamos los elementos duplicados y con la funcion sorted, recorremos el arreglo de manera ordenada
box_array = ['glases', 'eraser', 'money', 'pencil', 'ball', 'book', 'notebook', 'money']
for dup in sorted(set(box_array)):
    print(dup)
'''

'''
# Operadores de comparacion

num1= 5
num2= 8

print(num1 < num2)
print(num1==num2)
print(num1>=num2)
print(num2 != num1)

# Comparadores and or y not

x = 6
y = x>5 and x<7 # obtenemos True si una de las comparaciones es verdadera simultaneamente
z = x>5 or x<7 # tenemos false unicamente cuando las dos comparaciones son falsas, devuelve verdadero si cualquiera de las dos comparaciones es verdadera o se cumple
o = not x>5 # obtenemos la respuesta contraria a la original

print(y)
print(z)
print(o)

# Comparando secuencias y otros tipos
'''
