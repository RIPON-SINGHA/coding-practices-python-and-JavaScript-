def main():
    number = int(input("Enter your number: "))
    result = isArmstrong(number)
    if(result):
        print(f"The number {number} is Armstrong")
    else:
        print(f"The number {number} is not Armstrong")

def isArmstrong(n): #153
    if n == 0:
        return True
    n = abs(n)
    number = n
    num = n
    arm = 0
    count = 0
    while n > 0:
        count = count + 1
        n = n // 10 # 15, 1, 0

    while number > 0:
        temp = number % 10 # 3, 5, 1
        arm = arm + pow(temp, count) # 27, 152, 153
        number = number // 10 # 15, 1, 0
        
        
    if arm == num:
        return True
    else:
        return False
    

main()