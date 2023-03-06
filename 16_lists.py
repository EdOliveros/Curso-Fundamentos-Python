numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['make a dishes', 'play videogames']
print(tasks)

types = [1, True, 'Hola']
print(types)
print(types[2])
print(numbers[0])

'''
Los strings no se pueden modificar como arrays
text = 'Hola'
text[0] = 'w'
'''

tasks[0] = 'Watch platzi courses'
print(tasks)

tasks[0] = 'Do the dishes'
print(tasks)

print(numbers[:3])
print(True in types)
print('Hola' in types)