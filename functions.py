#print()
#dir()
#type()

# Esas son funciones de codigo ya escrito

def hello(name):
    print("Hello ", name)


hello('Mayra')

def add(numberOne, numberTwo):
    return numberOne + numberTwo

print(add(10, 30))

suma = lambda numberOne, numberTwo: numberOne + numberTwo

print(suma(10, 30))