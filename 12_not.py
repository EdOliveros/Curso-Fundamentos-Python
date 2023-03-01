print(not True) # False
print(not False) # True

print('NOT AND')
print('Not, True and True => ', not (True and True))# False
print('Not, True and False => ', not (True and False)) # True
print('Not, False and True => ', not (False and True)) # True
print('Not, False and False => ', not (False and False)) # True

stock = input("Ingrese el numero de Stock => ")
stock = int(stock)

print(not (stock >= 100 and stock <= 1000))