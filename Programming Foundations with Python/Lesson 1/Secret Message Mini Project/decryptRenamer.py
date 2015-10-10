import os
import string

def removeNumbersFromFilesInDir(search_directory):
  search_directory = search_directory + os.sep +"Secret-Message"
  file_list = os.listdir(search_directory)
  for file_name in file_list:
    print("Old Filename: " + file_name)
    os.rename(search_directory+os.sep+ file_name, search_directory+os.sep+ file_name.translate(None, string.ascii_uppercase))
    print("New Filename: " +os.sep+  file_name.translate(None, string.ascii_uppercase))

##  os.chdir(saved_path)
    
search_directory = "C:\Users\William\Projects\python\Udacity\Programming Foundations with Python\Lesson 1\Secret Message Mini Project"

removeNumbersFromFilesInDir(search_directory)
