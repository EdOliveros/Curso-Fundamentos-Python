numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico', 'nico')

print(numbers)
print('0 => ', numbers[0])
print('-1 => ', numbers[-1])
print(type(numbers))


print(strings)
print(type(strings))

print(strings)
print(strings.index('zule'))

print(strings.count('nico'))

# Transformando una tupla a una lista
my_list = list(strings)
print(type(my_list))

my_list[1] = 'Juli'
print(my_list)


# Transformanfo una lista en una tupla

my_tuple = tuple(my_list)
print(my_tuple)
print(type(my_tuple))