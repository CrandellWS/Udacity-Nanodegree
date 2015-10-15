# [Nanodegree](https://www.udacity.com/nanodegree)

## [Programming Foundations with Python](https://www.udacity.com/course/ud036)
---

### [Lesson 3](https://www.udacity.com/course/viewer#!/c-ud036/l-997889780)
---

 Lesson 3 YouTube playlist ID: [PLBxMIgvbjWQgmvBhmcSOAWGKM3-9XAfBn](https://www.youtube.com/playlist?list=PLBxMIgvbjWQgmvBhmcSOAWGKM3-9XAfBn)

___


#### Notes

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

###### Info: Curriculum is subject to change at a future date, be sure to use the [Udacity dashboard](https://www.udacity.com/me#!/).
