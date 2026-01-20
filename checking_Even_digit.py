# here i am going to check if a integer only contains even numbers or not
# if i found one odd then it will return false and if not it will return true

def main():
    number = int(input("Enter the numebr: "))
    result = isAllEven(number)
    if result:
        print(f"Your number {number} contains all even numbers")
    else:
        print(f"Your number {number} does not contains all even numbers")

def isAllEven(n): #123054
    if n == 0:
        return True
    
    n = abs(n)
    
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            n = n // 10
        else:
            return False
    
    return True
        
main()