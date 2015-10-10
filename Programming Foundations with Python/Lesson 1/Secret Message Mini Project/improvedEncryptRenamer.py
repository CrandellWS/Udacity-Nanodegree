import os
import string
import random
import errno
import shutil

dataInputs = {}

def encryptDirFileNames():
  os.chdir(dataInputs["parent_directory"])
  letter_list = os.listdir("pngLetters")
  n = 0
##  upper() -> stackoverflow.com/a/9257122/1815624
  for l in dataInputs["SecretMessage"].upper() :
    n = n + 1
    nLetters = (random.choice(string.digits))
    nLetters = int(nLetters) + 1
    i=0
    fLetters = random.choice(string.ascii_uppercase)
    while i < nLetters:
      fLetters = fLetters + random.choice(string.ascii_uppercase)
      i = i + 1
    numLocation =  random.randint(1, len(fLetters))
    if(l == " "):
      l = "space"
    fLetters = fLetters[:numLocation] + str(n) + fLetters[numLocation:]
    ## from -> stackoverflow.com/q/5254445/1815624
    shutil.copy("pngLetters"+os.sep+l+".png", "My-Secret-Message"+os.sep+fLetters + ".png")

def pngLettersValidation():
  for l in string.ascii_uppercase:
    if(not os.path.isfile("pngLetters"+os.sep+l+".png")):
      raise ValueError("pngLetters"+os.sep+l+".png does not exsist please make sure you have all required png files (A.png-Z.png)")
  if(not os.path.isfile("pngLetters"+os.sep+"space.png")):
    raise ValueError("pngLetters"+os.sep+"space.png does not exsist please make sure you have all required png file (space.png)")
  getSecretMessage()
  
def getSecretMessage():
  SecretMessage =  ''
  while True:
    if all(x.isalpha() or x.isspace() for x in SecretMessage) and SecretMessage != '':
      break
    else:
      print("Your Secret Message can only contain Letters and Spaces \n ")
      SecretMessage = raw_input("\n Please Enter Your Secret Message To Encrypt:")
  print("Ok the Secret Message is: " + SecretMessage)
  dataInputs["SecretMessage"] = SecretMessage
  secretMessageDirCheck()

def secretMessageDirCheck():
  secretMessagePath = os.path.isdir(dataInputs["My-Secret-Message"] )
  if(secretMessagePath):
    print("Sorry, the My-Secret-Message folder has already been created please delete, rename or move it and try again.\n")
    print(dataInputs["My-Secret-Message"])
    waitForUserAndTryAgain()
  else:
    make_sure_path_exists(dataInputs["My-Secret-Message"])


def waitForUserAndTryAgain():
  ## cross-platform solution found at http://stackoverflow.com/a/1395006/1815624
  try:
    os.system('pause')  #windows, doesn't require enter
  except whatever_it_is:
    os.system('read -p "Press any key to continue"') #linux
  secretMessageDirCheck()


def make_sure_path_exists(path):
  ##from http://stackoverflow.com/a/5032238/1815624
  try:
    os.makedirs(path)
  except OSError as exception:
    raise
  encryptDirFileNames()
  
def pngLettersDirCheck():
  dataInputs["pngLetters"] = dataInputs["parent_directory"]+os.sep+"pngLetters"
  dataInputs["My-Secret-Message"] = dataInputs["parent_directory"]+os.sep+"My-Secret-Message"
  pngLettersPath = os.path.isdir(dataInputs["pngLetters"])
  if(not pngLettersPath):
    print("Sorry, that was not understood or the pngLetters folder was not found try again.")
    print(dataInputs["pngLetters"])
    getDirValue()
  else:
    pngLettersValidation()
    
def getDirValue():
  realPath = True
  ##Get directory Input from user
  while realPath:
    userInput = raw_input(" Please input the directory path that contains the folder "\
                          +"\n pngLetters"\
                          + "\n Do Not include trailing slash: ")
    realPath = not os.path.isdir(userInput)
    if(realPath):
      print("Sorry, that was not understood please use directory path as input.")
    else:
      dataInputs["parent_directory"] = userInput
      pngLettersDirCheck()

getDirValue()
