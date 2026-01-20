def main():
    number = int(input("Enter Your number: "))
    result = sumOfPrime(number)
    print(f"The sum of prime in your number {number} is {result}")

def sumOfPrime(n):
    if n <= 0:
        return 0
    sum = 0
    while n > 0:
        digit = n % 10
        if digit <= 1:
            isPrime = False
        else:
            isPrime = True
            for i in range(2, digit): 
                if digit % i == 0:
                    isPrime = False
                    break
                
        if isPrime:
            sum = sum + digit

        n = n // 10
    
    return sum

main()