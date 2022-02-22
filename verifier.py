def get_verifying_table(wl, answer, usr):
    list_verifier = []

    if usr not in wl.wordlist:
        raise ValueError("Not in wordlist")

    if len(usr) != 5 or len(answer) != 5:
        raise ValueError("superior len")

    for char in list(usr):
        list_verifier.append([char, "WHITE"])

    index = 0

    for pair in list_verifier:
        if index >= len(answer):
            break
        if pair[0] == answer[index]:
            pair[1] = "GREEN"
        elif pair[0] in answer:
            pair[1] = "YELLOW"
        else:
            pair[1] = "RED"

        index += 1

    return list_verifier


def verify(wl, answer):
    verifying_table = None

    while True:
        usr = input("> ")
        try:
            verifying_table = get_verifying_table(wl, answer, usr)
        except ValueError:
            print("Not in worldlist")

        if verifying_table is not None:
            if all([pair[1] == "GREEN" for pair in verifying_table]):
                print("Gagné !")
                break

        if verifying_table is not None:
            print([pair[1] for pair in verifying_table])
