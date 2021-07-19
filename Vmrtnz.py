class alphbeth: 
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ".", ",", "á", "é", "í", "ó", "ú", "à", "è", "ì", "ò", "ù", "ã", "õ", "â", "ê", "î", "ô", "û", "ä", "ë", "ï", "ö", "ü", "Ç", "Á", "É", "Í", "Ó", "Ú", "À", "È", "Ì", "Ò", "Ù", "Ã", "Õ", "Â", "Ê", "Î", "Ô", "Û", "Ä", "Ë", "Ï", "Ö", "Ü", "Ç", "!", "?", ":", "{", "}", "[", "]", "(", ")", "'", '"', "´", "`", "^", "~", "¨", "@", "#", "$", "%", "&", "*", "_", "+", "=", "-"]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    l = letters.__len__()

    def tranformToNumber(word : str):
        numberWord = 0

        for i in word:
            for j in range(M.l):
                if i == alphbeth.letters[j]:
                    numberWord += j

        return numberWord
    
    
    def tranformToNumbers(word : str):
        numberWord = [0] * word.__len__()

        count = 0

        for i in word:
            for j in range(M.l):
                if i == alphbeth.letters[j]:
                    numberWord[count] = j
                    count += 1

        return numberWord


M = alphbeth

def incriptWord(word):
    incWord = [""] * (word.__len__() + 1)

    count = 0

    for i in word:
        tmpBool = False

        alg = 1
        div = M.tranformToNumber(i) / 2

        for j in range(M.numbers.__len__()):
            if i == alphbeth.numbers[j]:
                incWord[count] = "-0" + alphbeth.numbers[j]
                count += 1
                tmpBool = True
            elif tmpBool == False:
                tmpBool = False

        if not tmpBool:
            incWord[count] = M.letters[M.l - M.tranformToNumber(i) - 1]

            if not i == " ":
                while div % 2 == 0 and div > 0:
                    alg += 1

                    incWord[count] = M.letters[int(M.l - div - 1)] + str(alg)

                    div = M.tranformToNumber(i) / alg - 1
            else:
                incWord[count] = " "
                
            count += 1

    res = ""

    for i in range(incWord.__len__()):
        res += incWord[i]
    
    if not M.numbers.__contains__(incWord[incWord.__len__() - 1]):
        res += str(alg)

    return res


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


def main(words):
    result = incriptWord(words)

    print(result)

    result = decriptWord(result)

    print(result)


if __name__ == "__main__":
    inp = input("\nR- ")

    while not inp == "":
        main(inp)
        inp = input("\nR- ")
