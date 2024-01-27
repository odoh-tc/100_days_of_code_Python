from turtle import Turtle, Screen
import random
tim = Turtle()
S = Screen()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
def different_shapes(num_of_sides):
    angle = 360 / num_of_sides
    for _ in range(num_of_sides):
        tim.forward(100)
        tim.right(angle)


for shapes in range(3, 11):
    tim.color(random.choice(colours))
    different_shapes(shapes)

S.exitonclick()
