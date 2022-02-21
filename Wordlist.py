class Wordlist:
    def __init__(self):
        self.wordlist = []

    def fill(self):
        f = open("./wordlist.txt")
        self.wordlist = [line.rstrip() for line in f.readlines()]
        f.close()

