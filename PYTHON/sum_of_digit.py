def main():
    number = int(input("Enter your number: "))
    result = sumDigit(number)
    print(f"The answer of sum of your digit is {result}")


def sumDigit(n): # 1234
    if n == 0:
        return 0
    digit_sum = 0
    n = abs(n)

    while n > 0:
        temp = n % 10 # 4, 3, 2, 1
        digit_sum = digit_sum + temp # 4, 7, 9, 10
        n = n // 10 # 123, 12, 1, 0 

    return digit_sum


main()
