def main():
    number = int(input("Enter your number: "))
    result = palin_check(number) 
    if(result):
        print(f"Your numebr {number} is a palindrome")
    else:
        print(f"Your number {number} is not a palindrome")
        
def palin_check(n): #121
    if n == 0:
        return True
    num = n
    rev = 0
    while (n > 0):
        temp = n % 10
        n = n // 10
        rev = rev * 10
        rev += temp

    
    if rev == num:
        return True
    else:
        return False
    
main()
