x = 3.3
print(x) # 3.3

y = 1.1 + 2.2
print(y) # 3.3000000000000003

print(x == y) # False

y_str = format(y, ".2g")
print("y como string = ", y_str)
print(y_str == str(x)) # True, forma de comparar por str

print('*' * 10)

print(y, x)

tolerance = 0.0001
print(abs(x - y) < tolerance) # True, si la resta es menor que la tolerancia, la diferencia sera soportada.