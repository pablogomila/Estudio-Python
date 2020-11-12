sueldo_presidente=int(input("Sueldo del Presidente: "))
print("Sueldo del Presidente: " + str(sueldo_presidente))

sueldo_director=int(input("Sueldo del Director: "))
print("Sueldo del Director: " + str(sueldo_director))

sueldo_jefearea=int(input("Sueldo del Jefe de Area: "))
print("Sueldo del Jefe de Area: " + str(sueldo_jefearea))

sueldo_administrativo=int(input("Sueldo Administrativo: "))
print("Sueldo Administrativo: " + str(sueldo_administrativo))

if sueldo_administrativo<sueldo_jefearea<sueldo_director<sueldo_presidente:
    print("Los sueldos son correctos")
else:
    print("Hay algo mal en los sueldos")

