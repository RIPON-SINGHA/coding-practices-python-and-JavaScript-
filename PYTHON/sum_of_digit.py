def main():
    number = float(input("Enter your number: "))
    result = sumDigit(number)
    print(f"The answer of sum of your digit is {result}")


def sumDigit(n): # 1234
    if n == 0:
        return 0
    rev = 0
    sum = 0
    n = abs(n)

    while n > 0:
        temp = n % 10 # 4, 3, 2, 1
        sum = sum + temp # 4, 7, 9, 10
        n = n // 10 # 123, 12, 1, 0 

    return sum


main()
