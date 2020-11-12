miTupla = ("Pablo", 35, "Jole", 33)

print(miTupla[:])

print("Cambio la tupla a lista")
miLista = list(miTupla)
print(miLista[:])

print("Lo vuelvo a pasar a tupla")
miTupla2 = tuple(miLista)
print(miTupla2[:])

print("Cuento los elementos en la tupla")
print(miTupla2.count("Jole"))

print("Pido el total de elementos en la tupla")
print(len(miTupla2))

print("Creo tupla nueva con un unico elemento para asegurar la coma")
miTupla3 = ("Pablo",)
print(len(miTupla3))

print("Desempaqueto la tupla para asignar valores a variables")
nombre1, anos1, nombre2, anos2 = miTupla
print(nombre1)
print(nombre2)
