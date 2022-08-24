x = 20

# if

if x  < 30:
    print("x is less than 30")
else:
    print("x is greater than 20")

# y asi con todas las variantes
#elif
color = "red"

if color == "red":
    print("the color is red")
elif color == "blue":
    print("the color is blue")
else:
    print("Any color")

# Ejemplo - condicionalesa anidadas

name = 'John'
lastname = 'Carter'

if name == 'John':
    if lastname == 'Carter':
        print('You are John Carter')
    else:
        print("You are not John Carter")
else:
    print("You are not John")

# Ejemplo - and

if x > 2 and x <= 10: print("x is greater than 2 and less than or equal to 10")

# Ejemplo - or

if x > 2 or x <= 20: print("x is greater than 2 and less than or equal to 20")

# Ejemplo - not

if (not(x==y)): print("x is not equal to y")