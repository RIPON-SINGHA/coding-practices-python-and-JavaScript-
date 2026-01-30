# square every digit of a number and concatenate them.
# for 765 => 493625

def square_digits(num): #765
    if num == 0:
        return 0
    
    res = 0
    ress = []
    
    while num > 0: 
        digit = num % 10 #5 6 7 
        res = pow(digit, 2) #25 36 49
        ress.insert(0, res) #49 36 25 
        num = num // 10 #76 7 0
        
    res = int("".join(map(str, ress)))    
    return res

print(square_digits(765))