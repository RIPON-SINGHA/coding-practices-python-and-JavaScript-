def main():
    number = int(input("Enter your number: "))
    result = countEvenDigit(number)
    print(f"The count of even number is your number {number} is {result}")


def countEvenDigit(n):
    if n == 0:
        return 1
    n = abs(n)
    count = 0

    while n > 0:
        digit = n % 10
        if(digit % 2 == 0):
            count = count + 1
        n = n // 10

    return count

main()