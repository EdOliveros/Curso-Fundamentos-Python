if True:
    print('Esto debe ejecutarse')

if False:
    print('Esto no debe ejecutarse')



pet = input("Cual es tu mascota favorita?  ")

if pet == 'perro':
    print("Tambien me encantan los perros!")

elif pet == 'gato':
    print('Espero tengas suerte!')

elif pet == 'pez':
    print('Eres lo maximo!')
else:
    print('No tienes ninguna mascota Interesante, Buuu')


'''
stock = int(input('Digita el Stock => '))

if stock >= 100 and stock <= 1000:
    print('El Stock es Correcto!')
else: 
    print('El Stock no es Correcto!')
'''

num = int(input('Ingresa un numero => '))

if num % 2 == 0:
    print("El numero es Par!")
else:
    print("El numero es Impar!")