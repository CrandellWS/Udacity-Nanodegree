# [Programming Foundations with Python](https://www.udacity.com/course/ud036)

## Lesson 1 Links
Link to Udacity for Lesson 1: https://www.udacity.com/course/viewer#!/c-ud036

YouTube playlist of Lesson 1: [PLBxMIgvbjWQi2B3cyOopGJJntd9NDC3iX](https://www.youtube.com/playlist?list=PLBxMIgvbjWQi2B3cyOopGJJntd9NDC3iX)

Letter Images for the mini project [Zip Archive](https://github.com/CrandellWS/Udacity-Nanodegree/blob/master/Programming%20Foundations%20with%20Python/Lesson%201/extras/Letters/png-letters.zip)

## Lesson 2 Links

YouTube playlist of Lesson 2: [PLBxMIgvbjWQh8zCPh-L9wz8NH12UPugOE](https://www.youtube.com/playlist?list=PLBxMIgvbjWQh8zCPh-L9wz8NH12UPugOE)

 Related Wikipedia Article: [https://en.wikipedia.org/wiki/Turtle_(robot)](https://en.wikipedia.org/w/index.php?title=Turtle_(robot)&oldid=635620745)

## Notes

### Note 1)
One of the videos titled "*[Opening a File](https://www.youtube.com/watch?v=f8CjSt624pc&list=PLBxMIgvbjWQi2B3cyOopGJJntd9NDC3iX&index=21)*" mentions to prefix the input string path variable with the letter **`r`** and it means "*raw path*" and it instructs python to take the string as it is and not to interpret it any other way. Example:

> `os.listdir("C:\OOP\prank")`
Compared to 
> `os.listdir(r"C:\OOP\prank")`

 What's to be noted is [***String Literals***](https://docs.python.org/reference/lexical_analysis.html#literals), after researching some it my belief that it means ***raw string*** not path, as it is used to interpret a path in context but in isolation it is handling a string.

### Note 2)
Also worth noting is [os.pathsep](https://docs.python.org/library/os.html#os.pathsep)
and [os.sep](https://docs.python.org/library/os.html#os.sep)
