def main():
    number = int(input("Enter your number: "))
    result = productOfDigit(number)
    print(f"The product of {number} is {result}")


def productOfDigit(n): #12034
    if n == 0:
        return 0
    n = abs(n)
    pro = 1
    while n > 0:
        temp = n % 10 # 4, 3, 0, 2, 1
        if temp != 0:
            pro = pro * temp # 4, 12, 24, 24
        n = n // 10 # 123, 12, 1, 0

    return pro
    
main()