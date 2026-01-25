# sum of digit using try except for input handling

def main():

    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Enter a valid integer number!")
        else:
            break

    res = sumOfDIgit(number)
    print(f"The sum of digit of this number {number} is {res}")

    

def sumOfDIgit(n): 
    if n == 0:
        return 0
    
    n = abs(n)
    sum = 0

    while n > 0:
        digit = n % 10 
        sum = sum + digit  
        n = n // 10 

    return sum


main()