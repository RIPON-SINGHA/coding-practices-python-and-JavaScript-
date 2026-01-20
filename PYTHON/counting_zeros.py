def main():
    number = int(input("Enter your number: "))
    result = countZeros(number)
    print(f"Your number {number} has {result} Zeros")


def countZeros(n): 
    if n == 0:
        return 1
    
    n = abs(n)
    count = 0

    while n > 0:
        digit = n % 10
        if digit == 0:
            count += 1
        n = n // 10

    return count

main()