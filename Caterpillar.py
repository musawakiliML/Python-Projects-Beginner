# import the module
import random
import turtle as t

# adds background color
t.bgcolor('yellow')

# create a caterpillar turtle
caterpillar = t.Turtle()
caterpillar.shape("square")
caterpillar.color("red")
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

# create a leaf turtle
leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (18, 6), (20, 20), (6, 18), (2, 14)) # leaf coordinates
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)




