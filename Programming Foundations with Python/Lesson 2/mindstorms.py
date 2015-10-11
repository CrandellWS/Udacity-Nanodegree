import turtle

def init_turtle(value_input):
  value_string = str(value_input)
  value_input = turtle.Turtle()
  window.register_shape(value_string+".gif")
  value_input.shape(value_string+".gif")
  value_input.pencolor("brown")
  return value_input
  
def draw_square(value_input):
  i = 0
  while(i< 4):
    ## parker's my dog but now here Parker listens. 
    value_input.left(90)
    value_input.forward(100)
    i = i + 1
  

def start_drawing(value_input):
  the_turtle = init_turtle(value_input)
  for n in range(0,36):
    print(n)
    draw_square(the_turtle)
    the_turtle.left(10)

## window is my screen
window = turtle.Screen()
window.bgcolor("green")
start_drawing("Parker")
window.exitonclick()
