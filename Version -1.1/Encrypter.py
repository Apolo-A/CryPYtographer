import json
from Alphabet import alphabet as M

version = "Version -1.1"

def return_file(filename):
    from os import getcwdb

    t_filename = getcwdb().__str__() + "\\\\" + version + "\\\\" + filename
    filename = ""

    passed_b = False # In "getcwdb", the returned string has the codification "b", so, it is to remove it codification.

    for letter in t_filename:
        if letter != "'":
            if (passed_b):
                filename += letter
            else: passed_b = True
    
    del t_filename

    return filename

class settings:
    import json

    data = {}

    def load_settings():
        with open(return_file("application_info.json"), "r") as f:
            settings.data = json.load(f)

    def save_settings():
        with open(return_file("application_info.json"), "w") as f:
            f.write("")
        
        with open(return_file("application_info.json"), "a") as f:
            json.dump({"last_version" : version, "save_history" : True}, f)


def encrypt_words(words):
    incWord = [""] * (words.__len__() + 1)

    count = 0

    for i in words:
        tmpBool = False

        alg = 1
        div = M.tranformToNumber(i) / 2

        for j in range(M.numbers.__len__()):
            if i == M.numbers[j]:
                incWord[count] = "-0" + M.numbers[j]
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

    if settings.data["save_history"] or settings.data["save_history"] == None: save_history(words, res)

    return res

def save_history(original_word, encrypted_word):
    with open(return_file("Last Encrypts.txt"), "a+") as f:
        if version != settings.data["last_version"] or settings.data["last_version"] == None:
            f.writelines("\n\n" + version + "\n\n")
        f.writelines(original_word + " -> " + encrypted_word + "\n")

def main(words):
    result = encrypt_words(words)

    print(result)

    settings.save_settings()


if __name__ == "__main__":
    inp = input("R- ")

    while not inp == "":
        settings.load_settings()

        main(inp)
        inp = input("\nR- ")