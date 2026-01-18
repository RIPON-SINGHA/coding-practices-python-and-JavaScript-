def main():
    number = int(input("Enter your number: "))
    result = rev_num(number)
    print(f"The reverse of the number {number} is {result}")


def rev_num(n):
    if n == 0:
        return 0
    rev = 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    while(n>0):
        temp = n % 10
        n = n // 10
        rev = rev * 10
        rev += temp
        
    return sign * rev

main()