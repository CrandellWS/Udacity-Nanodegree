# [Nanodegree](https://www.udacity.com/nanodegree)

## [Programming Foundations with Python](https://www.udacity.com/course/ud036)
---

### [Lesson 2](https://www.udacity.com/course/viewer#!/c-ud036/l-1004409226/)
---

Lesson [**2a** Link](https://www.udacity.com/course/viewer#!/c-ud036/l-1004409226/m-1013388851)

Lesson [**2b** Link](https://www.udacity.com/course/viewer#!/c-ud036/l-991551862/e-993510817/m-993510818)

Lesson [**2c** Link](https://www.udacity.com/course/viewer#!/c-ud036/l-993510820/e-999198926/m-1040428761)


 Lesson 2 YouTube playlist ID: [PLBxMIgvbjWQh8zCPh-L9wz8NH12UPugOE](https://www.youtube.com/playlist?list=PLBxMIgvbjWQh8zCPh-L9wz8NH12UPugOE)
___

#### Notes
---

##### 2a mini project

##### Other useful Links
  - [An Article on fractals for the 2a mini project](https://georgemdallas.wordpress.com/2014/05/02/what-are-fractals-and-why-should-i-care/)
    - [Better yet an article on turtle drawn fractals](http://www.fractalcurves.com/Turtle.html)
    - [Crash Course ...](http://www.algorithm.co.il/blogs/computer-science/fractals-in-10-minutes-no-6-turtle-snowflake/)
  - http://www.cs.swarthmore.edu/~richardw/cs21-s08/lab10.php
  - External Lab project [Lab 10: Turtles and Fractals](http://www.cs.swarthmore.edu/~richardw/cs21-s08/lab10.php)
  - [More on Fractals](http://natureofcode.com/book/chapter-8-fractals/)
  - [Examples for Turtle Graphics](http://jython.tobiaskohn.ch/turtlex.html)
  - [3d printing with Turtle Grpahics??](http://www.kanadas.com/papers-e/2015/04/supportless_horizontal_filamen.html)

##### lambda <- deserved it's own header
[The lambda expression](https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions) Sounded intimidating
  - They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition
```python
def mi(n):
	return lambda x: x + n
fn = mi(42)
```
`>>>fn(0)` = 42; `fn(1)` = 43; `fn(2)` = 44; ...

##### Fractal Python code for turtle

```python
##From a previously mentioned post I found this code intresting:
from turtle import *

def f(length, depth):
   if depth == 0:
     forward(length)
   else:
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
     left(120)
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)

f(500, 4)
```

```python
## Though it was the lambda statement that got my interest.
def koch(depth, size):
    if depth == 0:
        forward(size)
    else:
        recurse = lambda: koch(depth-1, size/3)
        recurse()
        left(60)
        recurse()
        right(120)
        recurse()
        left(60)
        recurse()

koch(3, 3**4)
```

##### Other Notes
Another mention is the `*identifier` meaning `*` if you don't already know read the -> [Python docs](https://docs.python.org/2.7/reference/expressions.html#calls)

___

###### Info: Curriculum is subject to change at a future date, be sure to use the [Udacity dashboard](https://www.udacity.com/me#!/).
