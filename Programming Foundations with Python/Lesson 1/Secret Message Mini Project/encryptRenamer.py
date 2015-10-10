import os
import string
import random

## Notice it is by design that the files names won't change unless
## The input folder contains a subfolder called "Secret-Message"
## don't want the possible opps...
## random selection learned from stackoverflow.com/a/2823331/1815624
## This program will add random letters to the filename.
## trying to keep this some what simple

def encryptDirFileNames(parent_directory):
  os.chdir(search_directory+os.sep+"Secret-Message")
  file_list = os.listdir(search_directory+os.sep+"Secret-Message")
  
  for file_name in file_list:
     nLetters = (random.choice(string.digits))
     nLetters = int(nLetters) + 1
     i=0
     fLetters = random.choice(string.ascii_uppercase)
     while i < nLetters:
       fLetters = fLetters + random.choice(string.ascii_uppercase)
       print(fLetters + file_name)
    
##def removeNumbersFromFilesInDir(search_directory):
##  # get file in folder
##
##  file_list = os.listdir(search_directory)
##  print(file_list + file_name)

##  saved_path = os.getcwd()
##  print("Current Working Directory is " + saved_path)
##
##  os.chdir(search_directory)
  
  
## # for each file in list rename it
##  for file_name in file_list:
##    print("Old Filename: " + file_name)
##    os.rename(search_directory+os.sep+ file_name, search_directory+os.sep+ file_name.translate(None, "0123456789"))
##    print("New Filename: " +os.sep+  file_name.translate(None, "0123456789"))

##  os.chdir(saved_path)
    
search_directory = "C:\Users\William\Projects\python\Udacity\Programming Foundations with Python\Lesson 1\Secret Message Mini Project"

encryptDirFileNames(search_directory)
