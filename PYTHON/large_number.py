def main():
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    result = largeNumber(num1, num2)
    if(result == "Both are equal!"):
        print("Both are equal!")
    elif(result):
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num2} is greater than {num1}")


def largeNumber(num1, num2):
    if num1 == num2:
        return "Both are equal!"
    return True if num1 > num2 else False

main()
