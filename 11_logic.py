# and
print('AND')
print('True and True => ', True and True) # True
print('True and False => ', True and False) # False
print('False and True => ', False and True) # False
print('False and False => ', False and False) # False

print(10 > 5 and 5 < 10) # True
print(10 > 5 and 5 > 10) # False

stock = input("Ingrese el numero de Stock => ")
stock = int(stock)

print(stock >= 100 and stock <= 1000)

# OR
print('OR')
print('True or True => ', True or True) # True
print('True or False => ', True or False) # True
print('False or True => ', False or True) # True
print('False or False => ', False or False) # False

role = input('Digita el Rol => ')

print(role == 'admin' or role == 'seller') # Si el rol es igual a 'admin' o es igual a 'seller', entonces es True.
