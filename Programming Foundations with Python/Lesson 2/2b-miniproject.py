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
    the_turtle.forward(size)
  else:
    recurse = lambda: koch2(the_turtle,depth-1, size/3)    
    recurse()
    the_turtle.left(60)
    recurse()
    the_turtle.right(120)
    recurse()
    the_turtle.left(60)
    recurse()
    
def init_turtle(value_input):
  value_string = str(value_input)
  value_input = turtle.Turtle()
  window.register_shape(value_string+".gif")
  value_input.shape(value_string+".gif")
  value_input.pencolor("brown")
  value_input.speed(0)
  value_input.right(45)
  value_input.up()
  value_input.backward(180)
  value_input.down()
  value_input.left(45)
  return value_input
  

def start_drawing_star(value_input):
  the_turtle = init_turtle(value_input)
  i = 0
  while(i < 3):
    i = i + 1
    start_drawing_snowflake(the_turtle)
    koch(the_turtle, 3, 3**4)
    the_turtle.right(360/3)
    koch2(the_turtle, 4, 3**3)
    the_turtle.right(360/3)

def start_drawing_snowflake(the_turtle):
  i = 0
  while(i < 4):
    i = i + 1
    koch(the_turtle, 4, 4**4)
    the_turtle.right(360/4)
    
## window is my screen
window = turtle.Screen()
window.bgcolor("green")
start_drawing_star("Parker")
window.exitonclick()
