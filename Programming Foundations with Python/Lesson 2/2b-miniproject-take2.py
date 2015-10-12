import turtle
import time

## Take 2

def w_for_william(the_turtle,depth, size):
  if depth < 2:
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
  value_input.pencolor("green")
  value_input.speed(0)
  return value_input
  
def try_it(value_input, sides, length):
  offset = 360 / sides
  the_turtle = init_turtle(value_input)
  the_turtle.fillcolor("orange")
  i = 0
  while(i < sides):
    print("i", i)
    the_turtle.fill(True)
    i = i + 1
    w_for_william(the_turtle, 3 , length)
    the_turtle.right(360/sides)
    n = 0
    while(n < sides):
      print("n", n)
      n = n + 1
      w_for_william(the_turtle, 3 , length * 2)
      the_turtle.right(360/sides*2)
      m = 0
      while(m < sides):
        print("m", m)
        m = m + 1
        w_for_william(the_turtle, 3 , length * 2*3)
        the_turtle.right(360/sides*2*3)
    the_turtle.fill(False)
    
  the_turtle.fillcolor("black")
  the_turtle.goto(0, -50)
  the_turtle.up()
  the_turtle.fill(True)
  the_turtle.circle(50)
  the_turtle.fill(False)
  the_turtle.down()
  the_turtle.ht()
    
## window is my screen
window = turtle.Screen()
window.bgcolor("black")
try_it("Sugar", 3, 3**3)
window.exitonclick()
