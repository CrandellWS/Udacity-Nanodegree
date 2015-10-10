import os

def rename_files():
  # get file in folder
  file_list = os.listdir("C:\Users\William\Projects\python\Udacity - Non Github\prank")
  print(file_list)
  
  # for each file in list rename it
  for file_name in file_list:
    os.rename(file_name, file_name.translate(None, "0123456789"))
    
rename_files()
