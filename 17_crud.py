# CRUD Create, Read, Update, and Delete, in array

# READ
numbers = [1, 2, 3, 4, 5]
print(numbers[0])

# UPDATE
numbers[-1] = 10
print(numbers)

numbers.append(700) # Insert in the final
print(numbers)

numbers.insert(0, '100') # Primero el indice de la posicion y luego el valor
print(numbers)

numbers.insert(3, 'hello')
print(numbers)

tasks = ['play videogames', 'todo2', 'todo3']

newArray = numbers + tasks
print(newArray)

print(newArray.index('todo2'))
index = newArray.index('todo2')
newArray[index] = 'todo change'

print(newArray)


# DELETE

newArray.remove('todo3')
print(newArray)

newArray.pop() # por default elimina el ultimo elemento, pero puedo darle el index
print(newArray)

newArray.pop(0)
print(newArray)

newArray.reverse()
print(newArray)

numbers_a = [1, 4, 6, 3]
numbers_a.sort() # de mayor a menor por default
print(numbers_a)

strings = ['re', 'ab', 'ed']
strings.sort() # por orden alfabetico por default
print(strings)

# newArray.sort() Este metodo no funciona con listas de tipos mezclados. ERROR