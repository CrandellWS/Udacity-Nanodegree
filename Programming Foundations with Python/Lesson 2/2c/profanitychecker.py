class ProfanityChecker:
    
    def __init__(self,file_):
        lines = {}
        ## see -> https://docs.python.org/2/library/functions.html#iter
        ## https://docs.python.org/2/library/functions.html?highlight=enumerate#enumerate
        with open(file_) as fp:
            for i, line in enumerate(iter(fp.readline, ''), start=1):
                lines[i] = self.process_line(line)
        self.lines = lines
        self.warning = False
        for line in lines:
            for word in lines[line]:
                if(isinstance(word, list)):
                    self.warning = True
                    print("line "+ str(line) +" contains a level " + str(word[1]) + " type of profanity")
        if(self.warning):
            print("Sorry but the file does not pass the profanity check")
        else:
            print("Sorry but the file does not pass the profanity check")
            
      
    def process_line(self, line):
        ## https://docs.python.org/2/library/string.html?highlight=split#string.split
        words = line.split()
        for i,word in enumerate(words):
            words[i] = self.run_check(word)
        return words

    def run_check(self, word):
        ## bad
        bad_words = {
            "shit":5,
            "fuck":5,
            "bitch":5,
            "asshole":5,
            "cunt":4,
            "bastard":3
        }
        return [word, bad_words[word]]if word in bad_words else word

