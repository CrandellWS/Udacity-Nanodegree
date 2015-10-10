import os

def removeNumbersFromFilesInDir(search_directory):
  # get file in folder

  file_list = os.listdir(search_directory)
  print(file_list)

##  saved_path = os.getcwd()
##  print("Current Working Directory is " + saved_path)
##
##  os.chdir(search_directory)
  
  
  # for each file in list rename it
  for file_name in file_list:
    print("Old Filename: " + file_name)
    os.rename(search_directory+os.sep+ file_name, search_directory+os.sep+ file_name.translate(None, "0123456789"))
    print("New Filename: " +os.sep+  file_name.translate(None, "0123456789"))

##  os.chdir(saved_path)
    
search_directory = "C:\Users\William\Projects\python\Udacity - Non Github\prank"

removeNumbersFromFilesInDir(search_directory)
