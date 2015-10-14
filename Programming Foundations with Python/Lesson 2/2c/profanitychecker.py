import json
import urllib
import sys
from distutils import util

class ProfanityChecker:
    
    def __init__(self,file_, online):
        lines = {}
        self.warning = False
        ## see -> https://docs.python.org/2/library/functions.html#iter
        ## https://docs.python.org/2/library/functions.html?highlight=enumerate#enumerate
        try:
            with open(file_) as fp:
                for i, line in enumerate(iter(fp.readline, ''), start=1):
                    if(online):
                        lines[i] = self.process_online(line)
                    else:
                        lines[i] = self.process_line(line)
            self.lines = lines
            for line in lines:
                if(online):
                    if(isinstance(lines[line], list)):
                        self.warning = True
                        print("line "+ str(line) +" contains profanity")
                else:
                    for word in lines[line]:
                        if(isinstance(word, list)):
                            self.warning = True
                            print("line "+ str(line) +" contains a level " + str(word[1]) + " type of profanity")
            if(self.warning):
                print("Sorry but the file does not pass the profanity check")
            else:
                print("The file does pass the profanity check")
        except IOError:
            ## https://docs.python.org/2/tutorial/errors.html
            print 'cannot open', file_
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
      
    def process_line(self, line):
        self.process_online(line)
        ## https://docs.python.org/2/library/string.html?highlight=split#string.split
        words = line.split()
        for i,word in enumerate(words):
            words[i] = self.run_check(word)
        return words

    def process_online(self, line):
        try:
            conn = urllib.urlopen("http://www.wdyl.com/profanity?q="+line)
            output = conn.read()
            conn.close()
            output = json.loads(output)
            if(util.strtobool(output["response"])):
                return [line, 10]
            else:
                return line
        except:
            return 
    
    def run_check(self, word):
        ## bad
        bad_words = dict(
            shit=5,
            fuck=5,
            bitch=5,
            asshole=5,
            cunt=4,
            bastard=3
        )

        return [word, bad_words[word]]if word in bad_words else word

## Local Dictionary Example
print("\n")
print("Local Dictionary Example")
print("\n")
file_ = ProfanityChecker("README.md", 1)
if(file_.warning):
    print("Warnings have been found")
else:
    print("No undesired words were found")


print("\n") * 3
    
## Online Remote Check Example

print("\n")
print("Online Remote Check Example")
file_ = ProfanityChecker("README.md", 0)
if(file_.warning):
    print("Warnings have been found")
else:
    print("No undesired words were found")

    
