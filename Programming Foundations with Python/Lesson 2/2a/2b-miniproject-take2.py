import turtle
import time

## Take 2

def w_for_william(the_turtle,depth, size):
  if depth == 1:
    the_turtle.forward(size)
  else:
    recurse = lambda: w_for_william(the_turtle,depth-1, size/6)
    recurse()
    the_turtle.right(60)
    recurse()
    the_turtle.left(120)
    recurse()
    the_turtle.right(120)
    recurse()
    the_turtle.left(120)
    recurse()
    the_turtle.right(60)
    recurse()
    
def init_turtle(value_input):
  value_string = str(value_input)
  value_input = turtle.Turtle()
  value_input.shape("turtle")
  value_input.pencolor("black")
  value_input.speed(0)
  return value_input
  
def try_it(value_input, sides, length):
  offset = 360 / sides
  the_turtle = init_turtle(value_input)
  the_turtle.fillcolor("black")
  the_turtle.fillcolor("green")
  the_turtle.up()
  the_turtle.goto(-20, -300)
  the_turtle.down()
  the_turtle.begin_fill()
  the_turtle.pensize(3)
  the_turtle.circle(300)
  the_turtle.end_fill()
  the_turtle.up()
  the_turtle.goto(20, -265)
  the_turtle.fillcolor("#FF6700")
  the_turtle.begin_fill()
  the_turtle.circle(265)
  the_turtle.end_fill()
  the_turtle.up()
  the_turtle.circle(265, 60)
  the_turtle.down()
  the_turtle.circle(265, -300)
  the_turtle.up()
  the_turtle.goto(100, 60)
  the_turtle.fillcolor("black")
  the_turtle.begin_fill()
  the_turtle.circle(120)
  the_turtle.end_fill()
  the_turtle.goto(0, 0)
  the_turtle.down()
  the_turtle.fillcolor("#EED202")
  the_turtle.pencolor("green")
  i = 0
  the_turtle.pensize(1)
  while(i < sides):
    the_turtle.begin_fill()
    n = 0
    while(n < sides):
      n = n + 1
      w_for_william(the_turtle, 3 , length * 2)
      the_turtle.right(360/sides*2)
      m = 0
      while(m < sides):
        m = m + 1
        w_for_william(the_turtle, 3 , length * 2*3)
        the_turtle.right(360/sides*2*3)
    i = i + 1
    w_for_william(the_turtle, 3 , length)
    the_turtle.right(360/sides)
    the_turtle.end_fill()
    
  the_turtle.goto(0, -50)
  the_turtle.fillcolor("green")
  the_turtle.pencolor("black")
    
## window is my screen
window = turtle.Screen()
window.bgcolor("#FF6700")
try_it("Sugar", 3, 3**3)
window.exitonclick()
