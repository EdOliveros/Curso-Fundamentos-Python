person = {
    'name': 'Ed',
    'lastname': 'Oliveros',
    'age': 24,
    'langs': ['JavaScript', 'Python']
}

print(person)

person['name'] = 'Santi'
person['age'] -= 50
person['langs'].append('Rust')
print(person)

del person['lastname']
person.pop('age')
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())