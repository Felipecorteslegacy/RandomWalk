import turtle as t
import random

the_turtle_walk = t.Turtle()
screen = t.Screen()


the_turtle_walk.pensize(6)
the_turtle_walk.speed("fastest")
directions = [0, 90, 180, 270]
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


for steps in range(5000):
    the_turtle_walk.color(random.choice(colours))
    the_turtle_walk.forward(15)
    the_turtle_walk.setheading(random.choice(directions))

screen.exitonclick()
