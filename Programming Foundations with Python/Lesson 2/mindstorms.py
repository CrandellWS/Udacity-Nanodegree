import turtle


def draw_square(value_input):
  value_string = str(value_input)
  value_input = turtle.Turtle()
  ## no there is not a screen import it is a function in turtle...
  print(value_string)
  print(value_string+".gif")
  window.register_shape(value_string+".gif")
  value_input.shape(value_string+".gif")
  value_input.pencolor("brown")
  value_input.fill(True)
  i = 0
  while(i< 4):
    ## parker's my dog but now here Parker listens. 
    value_input.left(90)
    value_input.forward(100)
    i = i + 1
  
  value_input.fill(False)
  value_input.up()
  value_input.forward(200)

  
def draw_circle(value_input):
  value_string = str(value_input)
  value_input = turtle.Turtle()
  window.register_shape(value_string+".gif")
  value_input.shape(value_string+".gif")
  value_input.up()
  value_input.right(45)
  value_input.forward(100)
  value_input.down()
  value_input.pencolor("red")
  value_input.circle(100)
  value_input.left(45)
  value_input.up()
  value_input.forward(66)

  
def draw_triangle(value_input):
  value_string = str(value_input)
  value_input = turtle.Turtle()
  window.register_shape(value_string+".gif")
  value_input.up()
  value_input.left(90)
  value_input.forward(100)
  value_input.down()
  value_input.shape(value_string+".gif")
  value_input.pencolor("orange")
  i =0 
  while(i < 2):
    value_input.left(60)
    value_input.forward(58)
    i = i + 1
  value_input.left(180 -30.45)
  value_input.forward(100)
  value_input.up()
  value_input.right(45)
  value_input.forward(133)
  
def start_drawing():
  draw_square("Parker")
##  draw_triangle("Sugar")
##  draw_circle("Lucy")


## window is my screen
window = turtle.Screen()
window.bgcolor("green")
start_drawing()
window.exitonclick()
