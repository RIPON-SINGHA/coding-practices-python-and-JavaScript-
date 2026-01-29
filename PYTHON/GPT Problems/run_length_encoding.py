# run length encoding (basic)
# input a string of consecutive characters and return the character with the count of that char's appearance before finding a new character
# "aaabbbbccddd" becomes "a3b4c2d3"

s = "aaabbbhhdddcccdd"
count = 1
res = "" 

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        res += s[i-1] + str(count)
        count = 1
    
res += s[-1] + str(count)

print(res)



# this is to print all the characters without its duplications using same logic without using set()

s = "aaabbbhhdddcccdd"
res = ""

for i in range(1, len(s)):
    if s[i] != s[i-1]:
        res += s[i-1]
    else:
        continue
res += s[-1]

print(res)