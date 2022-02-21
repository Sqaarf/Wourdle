class Wordlist:
    def __init__(self):
        self.wordlist = []

    def fill(self):
        with open("./wourdlist") as f:
            self.wordlist.append(f.readline())

