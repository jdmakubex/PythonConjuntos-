set_a = {'col','mex','bol'}
set_b = {'pe','bol'}

#Union
set_c = set_a.union(set_b)
print(set_c)

#Union utilizando operadores
print(set_a | set_b)

#Intersección
set_c = set_a.intersection(set_b)
print(set_c)
#Intersección con operadores
print(set_a & set_b)

#Diferencia
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

'''
Diferencia simétrica, todos los elementos de ambos conjuntos, excepto los que
tienen en común.
'''

set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)