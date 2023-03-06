'''
for element in range(1, 21):
    print(element)
'''

my_list = [23, 45, 65, 89, 43]
for i in my_list:
    print(i)


my_tupple = ('ed', 'juli', 'matias')
for i in my_tupple:
    print(i)

my_dict = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}
for key in my_dict:
    print(key, '=> ', my_dict[key])


for key, value in my_dict.items():
    print(key, '=> ', value)


people = [
    {
        'name': 'ed',
        'age': 24
    },
    {
        'name': 'zule',
        'age': 25
    },
    {
        'name': 'santi',
        'age': 28
    }
]


for person in people:
    print('name => ', person['name'])
    # for i in person:
        # print(i, '=> ', person[i])
