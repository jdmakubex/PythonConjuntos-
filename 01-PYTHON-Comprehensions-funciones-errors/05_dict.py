import random

'''
#Ejemplo ilustrativo
dict = {}
for i in range (1,5):
    dict[i] = i * 2

print(dict)

dict_v2 = {i : i * 2 for i in range (1,5)}
print(dict_v2)
'''


'''
countries = ['col','mex','bol','pe']
population = {}

#Contruyendo un diccionario integrando valores de una listra
for country in countries:
    population[country] = random.randint(1,100)
print(population)

#Misma tarea, pero utilizando dictionary conprenhentions
population_v2 = {country: random.randint(1,100) for country in countries }
print(population_v2)
'''

names = ['Nico','Zule','Santi']
ages = [12,56,98]
#la función zip une dos listas, por dfault muesdtra referencias de memoria, así que
#se le coloca list, para que queden unidos los valores sin referencias.
print(list(zip(names,ages)))

#Para unir 2 listas en un diccionario:
new_dict = { name: age for (name, age) in zip(names,ages) }
