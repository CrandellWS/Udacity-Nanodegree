import turtle

## window is my screen
window = turtle.Screen()
window.bgcolor("green")

def parker_draw_square():
  Parker = turtle.Turtle()
  ## no there is not a screen import it is a function in turtle...
  window.register_shape("Parker.gif")
  Parker.shape("Parker.gif")
  Parker.pencolor("brown")
  Parker.fill(True)
  i = 0
  while(i< 4):
    ## parker's my dog but now here Parker listens. 
    Parker.left(90)
    Parker.forward(100)
    i = i + 1
  
  Parker.up()
  Parker.forward(200)
  Parker.fill(False)
  
def lucy_draw_circle():
  Lucy = turtle.Turtle()
  window.register_shape("Lucy.gif")
  Lucy.shape("Lucy.gif")
  Lucy.up()
  Lucy.right(45)
  Lucy.forward(100)
  Lucy.down()
  Lucy.pencolor("red")
  Lucy.circle(100)
  Lucy.left(45)
  Lucy.up()
  Lucy.forward(66)
  
def sugar_draw_triangle():
  Sugar = turtle.Turtle()
  window.register_shape("Sugar.gif")
  Sugar.up()
  Sugar.left(90)
  Sugar.forward(100)
  Sugar.down()
  Sugar.shape("Sugar.gif")
  Sugar.pencolor("orange")
  i =0 
  while(i < 2):
    Sugar.left(60)
    Sugar.forward(58)
    i = i + 1
  Sugar.left(180 -30.45)
  Sugar.forward(100)
  Sugar.up()
  Sugar.right(45)
  Sugar.forward(133)
  
def start_drawing():  
  parker_draw_square()
  sugar_draw_triangle()
  lucy_draw_circle()

start_drawing()
window.exitonclick()
