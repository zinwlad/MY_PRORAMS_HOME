import turtle

def drawSquare(a, color):
    turtle.color(color)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(a)
        turtle.left(90)
    turtle.end_fill()
    turtle.forward(a)

turtle.speed(0)

# определяем размер и цвета для шахматной доски
square_size = 50
light_color = "white"
dark_color = "black"

# рисуем шахматную доску
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            drawSquare(square_size, light_color)
        else:
            drawSquare(square_size, dark_color)
    turtle.backward(square_size*8)
    turtle.right(90)
    turtle.forward(square_size)
    turtle.left(90)

turtle.done()