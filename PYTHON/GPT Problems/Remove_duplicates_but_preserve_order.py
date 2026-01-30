# Remove duplicates but preserve order
# "programming" => "progamin"


# That is the right way to impliment this problem and it is so simple
word = "programming"
res = ""

for ch in word:
    if ch not in res:
        res += ch

print(res)




# This is a different way to approach this problem usign character adjacency same as run length encoding

string = "circumference"
result = ""

for i in range(1, len(string)):
    if string[i] != string[i-1]:
        if string[i-1] not in result:
            result += string[i-1]
        elif string[i] not in result:
            result += string[i]
    else:
        if string[i] not in result:
            result += string[i]

print(result)
# this model is specifically not for this problem but as of logic building in depth of accessing the chars which has not been seen in the string twice can help.