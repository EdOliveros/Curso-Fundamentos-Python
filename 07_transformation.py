name = "Nicolas"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

print("Nicolas" + " Molina")
print(10 + 20)
# print("Nicolas" + 20)  Esto no es posible
print("Nicolas " + "20") # Esto si es posible

age = 24
print("Mi edad es: " + str(age))
print(f"Mi edad es {age}")

age = input("Escribe tu edad aqui => ")
print(type(age))
age = int(age)
age += 10
print(f"Tu edad en 10 años será {age}")