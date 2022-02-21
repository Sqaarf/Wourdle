import random

from GameUi import GameUi
from Wordlist import Wordlist
from verifier import verify

if __name__ == "__main__":
    wl = Wordlist()
    wl.fill()
    verifying_table = None
    answer = wl.wordlist[random.randint(0, len(wl.wordlist))]
    print(answer)
    while True:
        usr = input("> ")
        try:
            verifying_table = verify(wl, answer, usr)
        except ValueError:
            print("Not in worldlist")

        if verifying_table is not None:
            if all([pair[1]=="GREEN" for pair in verifying_table]):
                print("Gagné !")
                break

        if verifying_table is not None:
            print([pair[1] for pair in verifying_table])

    # gu = GameUi()
    # gu.gameloop()
