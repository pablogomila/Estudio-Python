miLista = ["Pablo", "Jole", "Sandra", "Chris"]

print("Lista completa")
print(miLista[:])
print("Lista en indice 1 porque arranca de 0")
print(miLista[1])
print("Lista indice -1 arranca del final")
print(miLista[-1])
print("Lista de rango incluye el primer numero y excluye el ultimo")
print(miLista[0:2])
print("Rango de lista sin indicar el inicio arranca del 0")
print(miLista[:2])
print("Range de lista indicando el inicio pero no el final")
print(miLista[1:])

print("Agrego un valor a la lista")
miLista.append("Roberto")
print("Imprimo lista")
print(miLista[:])
print("Agrego valor a la lista en indice 2")
miLista.insert(2, "Martha")
print("Imprimo lista entera")
print(miLista[:])

print("Uso extend para agregar varios valores")
miLista.extend(["Nestor", "Silvana", "Osvaldo"])
print("Imprimo lista entera")
print(miLista[:])

print("Consulto la posicion de un elemento en la lista (Jole)")
print(miLista.index("Jole"))

print("Pregunto si un valor esta en lista (Jole)")
print("Jole" in miLista)

print("Elimino un elemento especifico de lista")
miLista.remove("Silvana")
print(miLista[:])

print("Elimino el ultimo elemento de la lista con pop")
miLista.pop()
print(miLista[:])

print("Creo una lista nueva con otro nombre y la sumo a la primera")
miLista2 = ["Silvana", "Osvaldo"]
miLista3 = miLista + miLista2
print(miLista3[:])

print("Imprimo la lista varias veces seguidas")
print(miLista3[:]*3)
