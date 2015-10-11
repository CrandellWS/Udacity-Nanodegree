import turtle


## Though it was the lambda statement that got my interest.
def koch(the_turtle,depth, size):
  if depth == 0:
    the_turtle.forward(size)
  else:
    recurse = lambda: koch(the_turtle,depth-1, size/3)
    recurse()
    the_turtle.left(60)
    recurse()
    the_turtle.right(120)
    recurse()
    the_turtle.left(60)
    recurse()

def koch2(the_turtle,depth, size):
  if depth == 0:
    the_turtle.backward(size)
  else:
    recurse = lambda: koch2(the_turtle,depth-1, size/3)    
    recurse()
    the_turtle.left(60)
    recurse()
    the_turtle.right(120)
    recurse()
    the_turtle.left(60)
    recurse()

def my_koch(the_turtle,depth, size):
  if depth < 2:
    the_turtle.backward(size)
  else:
    recurse = lambda: my_koch(the_turtle,depth-1, size/3)
    recurse2 = lambda: my_koch(the_turtle,depth-1, size/6)
    recurse()
    the_turtle.left(60)
    recurse()
    the_turtle.right(120)
    recurse2()
    the_turtle.left(120)
    recurse()
    the_turtle.right(120)
    recurse()
    the_turtle.left(120)
    recurse2()
    the_turtle.right(120)
    recurse()
    the_turtle.left(60)
    recurse()
    
def init_turtle(value_input):
  value_string = str(value_input)
  value_input = turtle.Turtle()
##  window.register_shape(value_string+".gif")
##  value_input.shape(value_string+".gif")
  value_input.shape("turtle")
  value_input.pencolor("brown")
  value_input.speed(0)
  value_input.right(45)
  value_input.up()
##  value_input.backward(180)
  value_input.down()
  value_input.left(45)
  return value_input
  
def try_it(value_input):
  the_turtle = init_turtle(value_input)
  i = 0
  while(i < 18):
    the_turtle.left(99)
    the_turtle.forward(216)
    the_turtle.backward(216)
    the_turtle.right(90)
    i = i + 1
    my_koch(the_turtle, 3, 18)
    the_turtle.right(360/18)

def start_drawing_star(value_input):
  the_turtle = init_turtle(value_input)
  i = 0
  while(i < 3):
    i = i + 1
    start_drawing_snowflake(the_turtle)
    koch(the_turtle, 3, 3**4)
    the_turtle.right(360/3)
    koch2(the_turtle, 3, 3**3)
    the_turtle.right(360/3)

def start_drawing_snowflake(the_turtle):
  the_turtle = init_turtle(the_turtle)
  i = 0
  the_turtle.left(240)
  while(i < 3):
    i = i + 1
    koch2(the_turtle, 1, 3**4)
    the_turtle.left(360/3)
    
## window is my screen
window = turtle.Screen()
window.bgcolor("green")
##start_drawing_snowflake("Parker")
try_it("Parker")
window.exitonclick()
