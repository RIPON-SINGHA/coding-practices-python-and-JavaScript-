# counting different of character in a string

def main():
    word = input("Enter your string: ")
    result = countChar(word)
    print(result)


def countChar(w):
    if w == 0:
        return 1
    elif w == "":
        return 0
    
    digCount = 0
    alphaCount = 0
    spaceCount = 0
    specialCount = 0
    for ch in w:
        if '0' <= ch <= '9':
            digCount += 1
        elif ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
            alphaCount += 1
        elif ch == ' ':
            spaceCount += 1
        else:
            specialCount += 1

    return digCount, alphaCount, spaceCount, specialCount

main()
