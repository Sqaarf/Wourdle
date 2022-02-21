def verify(wl, answer, usr):
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
