x = (1, 2, 3) # tupla

print(x)

# Meses
months = ('January', 'February', 'March', 'April')

print(months)

# funcion

tuple()

# no sirve x = (1) sera tomado como int pero si se pone x = (1,) sera tomado en cuenta como tupla

x = (1, 2, 3, 4, 5)

print(x[4]) # = 5

del x # sirve para eliminar la tupla

# Las tulplas se usan en diccionarios
# ejemplo - las tuplas son los numeros de latitud en un diccionario

locations ={
    (35.12312, 39.000) : "Tokio",
    (30.12312, 39.000): "New york"
}