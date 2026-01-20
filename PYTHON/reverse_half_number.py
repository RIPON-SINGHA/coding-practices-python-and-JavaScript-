# here i am going to reverse an integer but only last half of it. if the number is 123456 then it will return 654

def main():
    number = int(input("Enter your number: "))
    result = revHalfInt(number)
    print(result)


def revHalfInt(n):
    if n == 0:
        return 0
    
    n = abs(n)
    num = n
    Totalcount = 0

    while n > 0:
        Totalcount += 1
        n = n // 10

    count = Totalcount // 2
    rev = 0

    while count > 0:
        digit = num % 10
        rev = rev * 10
        rev = rev + digit
        num = num // 10
        count -= 1

    return rev

main()



