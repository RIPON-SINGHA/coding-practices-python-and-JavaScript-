# reversing a string from first and last half and keeping same the middle index character

def main():
    word = input("Enter your String: ")
    reverseStr = revStr(word)
    print(f"this is the reverse of your String {word}: {reverseStr}")
def revStr(w):
    result = ""
    mid = len(w) // 2

    # firstHalf = string[:mid]
    # secondHalf = string[mid:]

    for i in range(mid - 1, -1, -1):
        result += w[i]

    if len(w) % 2 != 0:
        result += w[mid]
        secondHalf = mid+1
    else:
        secondHalf = mid

    for j in range(len(w) - 1, secondHalf - 1, -1):
        result += w[j]
        
    return result 

main()