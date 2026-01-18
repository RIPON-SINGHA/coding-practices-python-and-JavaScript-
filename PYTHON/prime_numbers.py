# Checking if a number is prime numner or not
import math

def main():
    number = int(input("Enter your number: "))
    result = isPrime(number)
    if(result):
        print(f"The number {number} is a Prime number")
    else:
        print(f"The number {number} is not a Prime number")


def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

main()



# Returning the First divisor of a non prime number

import math

def main():
    number = int(input("Enter your number: "))
    result = first_divisor(number)
    if result == 0:
        print(f"The number {number} has no divisor")
    elif result == 1:
        print(f"The first divisor of {number} is {result}")
    else:
        print(f"The first divisor of {number} is {result}")

def first_divisor(n): #33
    if n <= 1:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return 2
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            div = i
            return div
    return 0

main()
