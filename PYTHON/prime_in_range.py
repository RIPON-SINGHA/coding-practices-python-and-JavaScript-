# Using two functions

import math

def main():
    number = int(input("Enter your range: "))
    rangePrime(number)

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


def rangePrime(num): #10
    if num <= 1:
        print("No prime Number")
    else:
        for i in range(2, num + 1):
            if isPrime(i):
                print(i, end = " ")

main()








# Using only one function

def main():
    number = int(input("Enter your range: "))
    rangePrime(number)



def rangePrime(n):
    if n <= 1:
        print("No prime numbers")
        return
    
    for i in range(2, n + 1):
        if i == 2:
            print(i, end = " ")
            continue
        elif i % 2 == 0:
            continue    
    
        isPrime = True
        for j in range(3, int(math.sqrt(i))+ 1, 2):
            if i % j == 0:
                isPrime = False
                break
        
        if isPrime:
            print(i, end = " ")

main()