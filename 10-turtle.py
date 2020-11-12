import turtle

def correcto():
    turtle.right(45)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)

def error():
    turtle.right(45)
    turtle.forward(135)
    turtle.left(135)
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(135)

peso_elefante = 3000
peso_mosca = 0.01

if peso_elefante > peso_mosca:
    correcto()




turtle.done()
