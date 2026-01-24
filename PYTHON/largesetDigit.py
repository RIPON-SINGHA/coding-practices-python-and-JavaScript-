# Finding the largest digit in a number

def main():
    number = int(input("Enter a number: "))
    result = largeDigit(number)
    if result > 0:
        print(f"The largest digit from your number{number} is {result}")
    else:
        print("No largest number")

def largeDigit(n):
    if n == 0:
        return 0
    
    n = abs(n)
    big = 0
    
    while n > 0:
        digit = n % 10
        
        if big < digit:
            big = digit
        
        n = n // 10
        
    return big
    
main()