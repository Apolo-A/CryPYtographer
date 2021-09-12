class alphabet: 
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", ".", ",", "á", "é", "í", "ó", "ú", "à", "è", "ì", "ò", "ù", "ã", "õ", "â", "ê", "î", "ô", "û", "ä", "ë", "ï", "ö", "ü", "Ç", "Á", "É", "Í", "Ó", "Ú", "À", "È", "Ì", "Ò", "Ù", "Ã", "Õ", "Â", "Ê", "Î", "Ô", "Û", "Ä", "Ë", "Ï", "Ö", "Ü", "Ç", "!", "?", ":", "{", "}", "[", "]", "(", ")", "'", '"', "´", "`", "^", "~", "¨", "@", "#", "$", "%", "&", "*", "_", "+", "=", "-"]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    l = letters.__len__()

    def tranformToNumber(word : str):
        numberWord = 0

        for i in word:
            for j in range(alphabet.l):
                if i == alphabet.letters[j]:
                    numberWord += j

        return numberWord
    
    
    def tranformToNumbers(word : str):
        numberWord = [0] * word.__len__()

        count = 0

        for i in word:
            for j in range(alphabet.l):
                if i == alphabet.letters[j]:
                    numberWord[count] = j
                    count += 1

        return numberWord