demo_list = [1, 'hello', 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']

# Constructor

numberList = list ((1, 2, 3, 4))
print(numberList)

r = list(range (1, 11)) # llega hasta 1 numero antes del segundo valor de rango
print(r)

print(dir(colors)) # ¿Que puedo ejecutar con listas?

print(len(colors))

print(colors[1])

print('green' in colors)

print(colors)
colors[1] = "yellow"
print(colors)

#METODOS

# colors.extend(['violet', 'yellow'])

# colors.insert(1, 'violet')

# print(colors)

# colors.pop()

# colors.remove("green")

colors.sort()

print(colors)