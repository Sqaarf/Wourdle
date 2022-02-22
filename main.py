import random

from GameUi import GameUi
from Wordlist import Wordlist
from verifier import verify

if __name__ == "__main__":
    wl = Wordlist()
    wl.fill()

    answer = wl.wordlist[random.randint(0, len(wl.wordlist))]
    print(answer)

    # verify(wl, answer)



    gu = GameUi()
    gu.gameloop()
