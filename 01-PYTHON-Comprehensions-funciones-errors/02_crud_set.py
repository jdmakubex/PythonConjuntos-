'''
Funciones de set:

    add(): Añade un elemento.
    update(): Añade cualquier tipo de objeto iterable como: listas, tuplas.
    discard(): Elimina un elemento y si ya existe no lanza ningún error.
    remove(): Elimina un elemento y si este no existe lanza el error “keyError”.
    pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
    clear(): Elimina todo el contenido del conjunto.
'''

print('\n conjunto de países \n');
set_contries = {'col', 'mex', 'bol','bol'};

print('\n Tamaño del conjunto \n');
size = len(set_contries);
print(size);

print('\n Para saber si algun elemento pertenece  al conjunto \n');
print('col' in set_contries)
print('pe' in set_contries)

'''
add  sirve para agregar un elemento al conjunto
'''

set_contries.add('pe')

set_contries.add('pe') #Aunque lo agregue 2 veces solo se agrega una vez

print(set_contries)

'''
update  sirve para actualizar un conjunto
'''

#En este ejemplo se agrega un subconjunto al conjunto
set_contries.update({'arg','ecu','pe'})
print(set_contries)

'''
remove  sirve para borrar un elemento del  conjunto
'''
set_contries.remove('col')
print(set_contries)


'''
discard  sirve para borrar un elemento del  conjunto
Pero si no existe el elemento no proboca error.
'''
set_contries.discard('esp')
print(set_contries)


'''
clear    Elimina todos los elementos del conjunto
'''
set_contries.clear()
print(set_contries)