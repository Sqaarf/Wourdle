from GameUi import GameUi
from Wordlist import Wordlist


if __name__ == "__main__":
    wl = Wordlist()
    wl.fill()

    gu = GameUi()
    gu.gameloop()
