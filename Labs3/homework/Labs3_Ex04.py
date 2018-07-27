from turtle import *
from Labs3_Ex03 import draw_square

for i in range(30):
    draw_square(i*5, 'red')
    left(17)
    penup()
    forward(i*2)
    pendown()
