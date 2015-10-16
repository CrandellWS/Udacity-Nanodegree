# [Nanodegree](https://www.udacity.com/nanodegree)

## [Programming Foundations with Python](https://www.udacity.com/course/ud036)
---

### [Lesson 3](https://www.udacity.com/course/viewer#!/c-ud036/l-997889780)
---

 Lesson 3 YouTube playlist ID: [PLBxMIgvbjWQgmvBhmcSOAWGKM3-9XAfBn](https://www.youtube.com/playlist?list=PLBxMIgvbjWQgmvBhmcSOAWGKM3-9XAfBn)

___

#### Notes
---

##### Handling Import Exceptions
 - http://stackoverflow.com/a/1618880/1815624
 - https://docs.python.org/2/library/__main__.html
 - https://docs.python.org/3/library/exceptions.html
 ```python
if __name__ == '__main__':
    try:
        import donothavethis
        import orthat

        donothavethis.main()
        orthat.main()
    except ImportError as error:
        print(error)
```

___

#### Links
---

  - [ Python Classes ](https://docs.python.org/tutorial/classes.html)
  - [ Instance Method ](https://docs.python.org/c-api/method.html)
  - <a href ="https://en.wikipedia.org/w/index.php?title=Constructor_(object-oriented_programming)&oldid=677805544#Python">Constuctors</a>
  - [ Random Remarks ](https://docs.python.org/tutorial/classes.html#random-remarks)
  - [ Exceptions ](https://docs.python.org/library/exceptions.html)
  - [ Python Data Model ](https://docs.python.org/reference/datamodel.html)
  - [ Class and Instance Variables ](https://docs.python.org/tutorial/classes.html#class-and-instance-variables)
  - [ Private Variables and Class-local References ](https://docs.python.org/tutorial/classes.html#private-variables-and-class-local-references)
___

###### Info: Curriculum is subject to change at a future date, be sure to use the [Udacity dashboard](https://www.udacity.com/me#!/).
