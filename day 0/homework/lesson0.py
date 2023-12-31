from turtle import *
# we want to paint a house
# grass
# bgcolor("green") 
# speed(30)
width(7)
color("purple")
begin_fill()


#step 1: draw a square
shape("turtle")
forward(200)
left(90)
forward(200) 
left(90)
forward(200)
left(90)
forward(200)       
left(90)
end_fill()
# end of square


# drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


# draw first window
left(120)
penup()
goto(150,180)
pendown()
color("blue")
begin_fill()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
end_fill()


# draw second window
right(180)
penup()
goto(50,180)
pendown()
color("blue")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
end_fill()
hideturtle()
exitonclick()