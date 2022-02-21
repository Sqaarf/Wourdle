class Word:
    def __init__(self, str):
        if len(str) == 5:
            self.str = str
        else:
            raise ValueError

    def __str__(self):
        return self.str
