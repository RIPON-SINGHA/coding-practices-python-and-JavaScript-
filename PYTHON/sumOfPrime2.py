# adding prime numbers till the range given by user
import math
def main():
    Range = int(input("Enter Range: "))
    result = sumOfPrime(Range)
    print(result)


def sumOfPrime(r):
    if r <= 1:
        print("No Prime numbers")
        return
    
    sum = 0
    for i in range(2, r + 1):
        if i == 2 :
            sum += i
            continue
        elif i % 2 == 0:
            continue

        isPrime = True
        for j in range(3, int(math.sqrt(i))+1, 2):
            if i % j == 0:
                isPrime = False
                break
        
        if isPrime:
            sum += i
    
    return sum

main()