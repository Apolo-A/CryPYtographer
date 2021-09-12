from Alphabet import alphabet as M

def decriptWord(word):
    decWord = ""

    for i in range(word.__len__() - 1):
        if word[i] == "-" and word[i + 1] == "0":
            decWord += word[i + 2]
            i += 2
        elif not M.letters.__contains__(word[i + 1]) and M.letters.__contains__(word[i]):
            decWord += M.letters[(M.tranformToNumber(word[i] * int(word[i + 1])) - M.l) * -1 - 1 * int(word[i + 1])]
        elif M.letters.__contains__(word[i]):
            if not word[i] == " ":
                decWord += M.letters[(M.tranformToNumber(word[i]) - M.l) * -1 - 1]
            else:
                decWord += " "
        else:
            decWord += ""

    return decWord

def main(word):
    result = decriptWord(word)
	
    print(result)

if __name__ == "__main__":
    inp = input("R- ")

    while not inp == "":
        main(inp)
        inp = input("\nR- ")