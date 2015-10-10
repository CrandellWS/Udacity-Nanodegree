import os
import string

dataInputs = {}
  
def mySecretMessageDirCheck():
  dataInputs["My-Secret-Message"] = dataInputs["parent_directory"]+os.sep+"My-Secret-Message"
  secretMessagePath = os.path.isdir(dataInputs["My-Secret-Message"] )
  if(not secretMessagePath):
    print("Sorry, that was not understood or the My-Secret-Message folder was not found try again.")
    print(dataInputs["My-Secret-Message"])
    getDirValue()
  else:
    removeNumbersFromFilesInDir()
    
def getDirValue():
  realPath = True
  ##Get directory Input from user
  while realPath:
    userInput = raw_input(" Please input the directory path that contains the folder "\
                          +"\n My-Secret-Message"\
                          + "\n Do Not include trailing slash: ")
    realPath = not os.path.isdir(userInput)
    if(realPath):
      print("Sorry, that was not understood please use directory path as input.")
    else:
      dataInputs["parent_directory"] = userInput
      mySecretMessageDirCheck()
      
def removeNumbersFromFilesInDir():
  file_list = os.listdir(dataInputs["My-Secret-Message"] )
  for file_name in file_list:
    print("Old Filename: " + file_name)
    os.rename(dataInputs["My-Secret-Message"] +os.sep+ file_name,dataInputs["My-Secret-Message"] +os.sep+ file_name.translate(None, string.ascii_uppercase))
    print("New Filename: " +os.sep+  file_name.translate(None, string.ascii_uppercase))

getDirValue()
