- Which function did you use?
- What does your program do?
- What problems (if any) did you run into?

## Used Functions ##

 - open() https://docs.python.org/2/library/functions.html#open
 - iter() https://docs.python.org/2/library/functions.html#iter
 - enumerate() https://docs.python.org/2/library/functions.html#enumerate
 - print() https://docs.python.org/2/library/functions.html#print
 - str() https://docs.python.org/2/library/functions.html#str
 - isinstance() https://docs.python.org/2/library/functions.html#isinstance
 - dict() https://docs.python.org/2/library/functions.html#func-dict
    - https://docs.python.org/2/library/stdtypes.html#typesmapping
 - list https://docs.python.org/2/library/functions.html?highlight=iter#list

## What the Program Does ##

 - Converts file path to object which contains
  - `warning` returns a  boolean value
  - `lines` returns a tuple (list of lists)
    - each `line` is a line of text from the file
        - contains a list of words
            - bad words are list types
            - other words are strings


[GitHub link to the source code](https://github.com/CrandellWS/Udacity-Nanodegree/tree/b8c82d318364125bad5dea8dd7c6cf826e85b9c3/Programming%20Foundations%20with%20Python/Lesson%202/2c)


## Problems ##

Tried to work with [`set()`](https://docs.python.org/2/library/functions.html?highlight=enumerate#func-set) and it seems like it could be used, may even be an improvement from what I have but I used **`list()`** and **`dict()`** instead.

While building the class I struggled some with understanding the first variable of a function was required. Found this question and answer http://stackoverflow.com/q/68282/1815624 helpful.

# Profanity Checker

## For Lesson 2c Profane words are used

### A basic text file is required

This file will be checked for profanity with a dictionary of words to filter.

The word bastard is being used for test purposes.

As well as this shit

Thank you for your understanding
