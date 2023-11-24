'''
Los sets en Python son una estructura de datos usada para almacenar elementos de una manera similar a las listas, pero con ciertas diferencias.

Crear un conjunto de Python Los set en Python son un tipo que permite almacenar varios elementos y acceder a ellos de una forma muy similar a las listas pero con ciertas diferencias:

Los elementos de un set son únicos, lo que significa que no puede haber elementos duplicados.

Los set son desordenados, lo que significa que no mantienen el orden de cuando son declarados. Sus elementos deben ser inmutables. Para entender mejor los sets, es necesario entender ciertos conceptos matemáticos como la teoría de conjuntos.

Para crear un set en Python se puede hacer con set() y pasando como entrada cualquier tipo iterable, como puede ser una lista. Se puede ver como a pesar de pasar elementos duplicados como dos 8 y en un orden determinado, al imprimir el set no conserva ese orden y los duplicados se han eliminado.
'''
#aunque se reipite 'bol' los conojuntos no duplican los datos
print('\n conjunto de strings \n');
set_contries = {'col', 'mex', 'bol','bol'}; #conjunto de strings
print (set_contries);
print (type(set_contries));

print('\n conjunto de numeros \n');
set_numbers = {1,2,2,3,4,5}; #conjunto de nuemeros
print(set_numbers);

#Conjunto de tipos
print('\n conjunto de tipos \n');
set_types = {'hola',False,12.12}
print(set_types);
print(type(set_types));

#Conjunto creado a partir de un string
print('\n Conjunto creado a partir de un string \n');
set_from_string = set('hola');
print(set_from_string);

#Conjunto creado a partir de una tupla
print('\n Conjunto creado a partir de una tupla \n');
set_from_tuple = set(('abc','cbv','as','abc'));
print(set_from_tuple);

#Conjunto creado a partir de una lista
print('\n Conjunto creado a partir de una lista \n');
numbers = [1,2,3,1,2,3,4] #Esta es una lista de numeros
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers); #Regresamos el resultado como lista
print('Regresamos el resultado como lista ', unique_numbers);

