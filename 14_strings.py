text = "Ella sabe programar en Python"

'''
print('JavaScript' in text)
print('Python' in text)

if 'Python' in text:
    print('Elegiste bien!!')
else:
    print('Tambien elegiste bien!!')
'''


size = len(text) # Los espacios cuentan
print(size)

print(text)
print(text.upper()) # MAYUSCULAS
print(text.lower()) # minusculas

print(text.count('a')) # contar las veces que aparece una letra o palabra en mi texto.

print(text.swapcase()) # Cambia minusculas por mayusculas y viceversa

print(text.startswith('Ella')) # Preguntar si mi string empieza con algo en especifico, respuesta booleana.
print(text.endswith('Rust')) # Preguntar si mi string termina con algo en especifico, respuesta booleana.

print(text.replace('Python', 'Go')) # Cambiar un texto por otro.


text2 = 'este es un titulo'
print(text2)
print(text2.capitalize()) # Primer caracter en mayuscula.
print(text2.title()) # Cada primer letra de cada palabra en mayuscula.
print(text2.isdigit()) # Es digito?
print('2345'.isdigit()) 