import random

user_option = input("piedra, papel o tijera? => ")
user_option = user_option.lower()

computer_option = 'tijera'


numero = random.randint(1, 3)

if numero == 1:
    computer_option = 'piedra'
elif numero == 2:
    computer_option = 'tijera'
elif numero == 3:
    computer_option = 'papel'

print("Computer is => ", computer_option)

''' 
if computer_option == user_option:
    print('Empate!')
elif computer_option == 'piedra' and user_option == 'papel':
    print('Ganaste!')
elif computer_option == 'tijera' and user_option == 'piedra':
    print('Ganaste!')
elif computer_option == 'papel' and user_option == 'tijera':
    print('Ganaste!')
else: 
    print('Perdiste!!')
'''

if computer_option == user_option:
    print('Empate!')
elif user_option == 'piedra':
    if computer_option == 'tijera':
        print('Piedra vence a Tijera')
        print('User Gano!')
    else:
        print('Piedra gana a Tijera')
        print('Computer gano!')
elif user_option == 'papel':
    if computer_option == 'piedra':
        print('Papel gana a Piedra')
        print('User gano!')
    else:
        print('Tijera gana a Papel')
        print('Computer gano!')
elif user_option == 'tijera':
    if computer_option == 'papel':
        print('Tijera gana a Papel')
        print('User gano!')
    else:
        print('Piedra gana a Tijera')
        print('Computer gano!')
