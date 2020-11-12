print("Evaluación")

nota_alumno=input("Introduce la nota: ")



def evaluacion(nota):
    valoracion="aprobado"
    if nota<6:
        valoracion="desaprobado"
    return valoracion



print(evaluacion(int(nota_alumno)))