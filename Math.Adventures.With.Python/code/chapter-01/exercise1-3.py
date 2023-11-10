from turtle import *

shape('turtle')

def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        left(120)
triangle()

done()
