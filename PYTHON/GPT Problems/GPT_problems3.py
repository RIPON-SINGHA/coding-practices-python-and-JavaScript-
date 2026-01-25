# checking a num is prime or not using try except for input and error handling
import math 

def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            break
        except ValueError:
            print("Enter a valid positive integer number")
        
    print(f"The number {number} is a Prime number") if isPrime(number) else print(f"The number {number} is not Prime number")


def isPrime(n): #5
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n))+ 1, 2):
        if n % i == 0:
            return False
    return True


main()
