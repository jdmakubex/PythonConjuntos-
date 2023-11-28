
'''
#Ejemplo generar una lista con un ciclo for
numbers = []
for element in range(1,11):
    numbers.append(element*2)

print(numbers)

# Ejemplo con list conprenhentions
numbers_v2 = [element * 2 for element in range (1,11) ]
print(numbers_v2)
'''


#Ejemplo generar una lista con un ciclo for
numbers = []
for i in range(1,11):
    #Si el residuo de la división es igual a cero lo agrega 
    if i % 2 == 0:
        numbers.append(i*2)

print(numbers)

# Ejemplo con list conprenhentions, agregando condiciones
numbers_v2 = [element * 2 for element in range (1,11) if element % 2 == 0]
print(numbers_v2)