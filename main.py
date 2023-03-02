def isItPassword(word):
    #NEW EDIT
    char = 0
    symbol = 0
    digi = 0
    if word.endswith('.') or word.endswith(',') or word.endswith(':') or word.endswith('?'):
        word = word[:len(word)-1]
    elif "'" in word:
        symbol = symbol - 1
    elif word.startswith('@'):
        word = word[1:]
    allWords = []
    if ":" in word:
        for x in word.split(":"):
            allWords.append(x)
    elif ":-" in word:
        for x in word.split(":-"):
            allWords.append(x)
    elif "-" in word:
        for x in word.split("-"):
            allWords.append(x)
    elif "=" in word:
        for x in word.split("-"):
            allWords.append(x)
    else:
        allWords.append(word)
    for newword in allWords:
        for c in newword:
            if c>='a' and c<='z':
                char = char + 1
            elif c>='0' and c<='9':
                digi = digi + 1
            else:
                symbol = symbol + 1
        if char > 0:
            #password = halodoc
            if symbol <= 0 and digi <= 0:
                pass
            elif char + symbol + digi >= 4:
                return True
            else:
                pass
        else:
            if char + symbol + digi >= 4:
                return True
    return False
def containsPassword(text):
    text = text.lower()
    if "password" in text:
        list = text.split()
        loc = []
        index = 0
        smallSet = []
        for word in list:
            if "password" in word:
                loc.append(index)
            index = index + 1
        for l in loc:
            #for i in range(l-4,l):
            #    if i>=0 and i<len(list):
            #        smallSet.append(list[i])
            for i in range(l,l+6):
                if i>=0 and i<len(list):
                    smallSet.append(list[i])
        print("\n\nPossible passwords are:")
        flag = False
        for word in smallSet:
            if isItPassword(word) == True:
                flag = True
                print("Can be a password : ", word)
        if flag == True:
            print("UnSafe")
            return True
        print("Safe")
    else:
        print("Safe")
        return False
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    containsPassword(input())
