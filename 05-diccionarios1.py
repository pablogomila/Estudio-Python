miDiccionario = {"Alemania": "Berlin", "Francia": "Paris", "UK": "Londres", "España": "Madrid"}

print("Consulto la cap de Francia")
print(miDiccionario["Francia"])

print("Agrego Argentina al diccionario")
miDiccionario["Argentina"] = "Buenos Aires"
print("Consulto la capital de Argentina")
print(miDiccionario["Argentina"])

print("Imprimo todo el diccionario")
print(miDiccionario)

print("Elimino Alemania del diccionario")
del miDiccionario["Alemania"]
print(miDiccionario)

print("Imprimo las KEYS del diccionario")
print(miDiccionario.keys())

print("Imprimo los Valores del diccionario")
print(miDiccionario.values())

print("Imprimo el largo del diccionario")
print(len(miDiccionario))