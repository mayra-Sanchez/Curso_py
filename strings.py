# aprender que podemos hacer con los strings

myStr = "Hello world"
# nos muestra propiedades y metodos de lo que se puede hacer con myStr

# print(dir(myStr))

print(myStr.upper()) # Mayuscula
print(myStr.lower()) # Minuscula
print(myStr.swapcase()) # Cambiar los mayus a minus y viceversa
print(myStr.capitalize()) # Deja unicamente la primera letra en mayuscula
print(myStr.replace("Hello","Bye")) # Reemplazar una palabra por otra
print(myStr.count("l")) # Conteo de letras en la variable

print(myStr.startswith("He")) # tiene que salir True - quiere decir que la variable inicia por he
print(myStr.endswith("world")) # tiene que salir True - quiere decir que la variable termina por world

print(myStr.split("o")) # Crea una lista
print(myStr.find("o")) # ubicacion de una letra de la variable
print(len(myStr)) # imprime la longitud - inicia desde 0

print(myStr.index("e")) # ubicacion de una letra de la variable

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4])

myStrName = "May"
print("My name is " + myStrName)
print(f"My name is {myStrName}")
print("My name is {0}".format(myStrName))