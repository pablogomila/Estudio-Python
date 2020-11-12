print("Verificacion de Nota")

nota_alumno=int(input("Tu nota: "))

if nota_alumno<3:
    print("No satisfactorio")
elif nota_alumno<6:
    print("Satisfactorio")
elif nota_alumno<8:
    print("Aprobado")
elif nota_alumno<=10:
    print("Promocionado")


print("Fin del programa")