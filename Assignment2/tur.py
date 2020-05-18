from turtle import *
speed(-1)

for edge in range (3, 7):
    for i in range (edge):
        forward(100)
        left(360/edge)
        if edge == 3 or edge == 5:
            color('blue')
        else:
            color('red')

mainloop()
