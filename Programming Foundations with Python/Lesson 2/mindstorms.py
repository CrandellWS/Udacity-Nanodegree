import turtle

def draw_square():
  window = turtle.Screen()
  window.bgcolor("green")
  i = 0
  Parker = turtle.Turtle()
  while(i < 4):
    i = i + 1
    ## parker's my dog but now here Parker listens. 
    Parker.forward(100)
    Parker.right(90)
  
  window.exitonclick()

draw_square()  
