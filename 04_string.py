name = "Edgar"
print(name)

last_name = "Oliveros"
print(last_name)

full_name = name + " " + last_name
print(full_name)

quote = "I'm Edgar"
print(quote)

quote2 = 'She said "Hello" '
print(quote2)

# format 
template = "Hola, mi nombre es " + name + ", y mi apellido es " + last_name + "."
print("V1", template)

template = "Hola, mi nombre es {}, y mi apellido es {}.".format(name, last_name)
print("V2, format", template)

template = f"Hola, mi nombre es {name}, y mi apellido es {last_name}."
print("V3, f", template)