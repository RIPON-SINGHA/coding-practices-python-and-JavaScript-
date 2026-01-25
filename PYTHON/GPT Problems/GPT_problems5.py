# checking the largest digit in a number but using try except for input handling

def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            print(f"The largest digit in your number {number} is {largeDigit(number)}")
            break
        except ValueError:
            print("Enter a valid integer number!")



def largeDigit(n):
    if n == 0:
        return 0
    
    n = abs(n)
    large = 0
    
    while n > 0:
        digit = n % 10

        if large < digit:
            large = digit
        
        n = n // 10

    return large

main()