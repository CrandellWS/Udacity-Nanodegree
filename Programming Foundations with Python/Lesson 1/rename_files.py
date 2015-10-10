import os

def rename_files():
  # get file in folder
  search_directory = "C:\Users\William\Projects\python\Udacity - Non Github\prank"
  file_list = os.listdir(search_directory)
  print(file_list)

  saved_path = os.getcwd()
  print("Current Working Directory is " + saved_path)

  os.chdir(search_directory)
  
  
  # for each file in list rename it
  for file_name in file_list:
    os.rename(file_name, search _directory+file_name.translate(None, "0123456789"))

  os.chdir(saved_path)
rename_files()
