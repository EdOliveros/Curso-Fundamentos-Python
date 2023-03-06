my_dict = {}
print(type(my_dict))

my_dict = {
    'name': 'ed',
    'age': 28,
    'single': True, 
}

print(my_dict)
print(len(my_dict))

print(my_dict['name'])
print(my_dict['age'])
print(my_dict.get('single'))
print(my_dict.get('sile'))

print('single' in my_dict)
print('sie' in my_dict)