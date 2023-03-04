text = 'Ella sabe Python'
print(text[0])
print(text[1])
print(text[2])
# print(text[98765]) si el index no existe, python arroja un error
size = len(text)
print('length => ', size)
print(text[size - 1])
print(text[-1]) # la ultima posicion, el ultimo index

# Slicing
print('Slicing')

print(text[0:5])
print(text[10:16])
print(text[:10]) # Puedo asumir siempre el inicio en el numero 0 
print(text[5:]) # tambien puedo asumir el final
print(text[:]) # asumo el inicio y el final
print(text[10:16:2]) # el ultimo digito le dice a python de a cuantos caracteres voy a saltar
print(text[::2])