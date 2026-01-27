# creating a calculator using try except to input and error handling

def main():
    while True:
        try:
            num1 = int(input("Enter your first number: "))
        except ValueError:
            print("Enter a valid number")
            continue

        while True:
                operator = input("Enter operator (+, -, *, /, %): ")
                if operator in "+-*/%":
                    break
                else:
                    print("Invalid operator! Try again!")

        try:
            num2 = int(input("Enter your second number: "))
        except ValueError:
            print("Enter a valid number")
            continue

        result = calculate(num1, num2, operator)

        if result is not None:
            print(f"{num1} {operator} {num2} = {result}")

        isEnd = input("Do you want to continue calculating? (y/n) ").lower()
        if isEnd == "n":
            print("Thank you for using my calculator.... Visit again")
            break

        


def calculate(n1, n2, op):
    match op:
        case "+":
            return add(n1, n2)
        case "-":
            return minus(n1, n2)
        case "*":
            return multiply(n1, n2)
        case "/":
            if n2 == 0:
                print("Can't divide by 0")
                return None
            else:
                return divide(n1, n2)
        case "%" :
            if n2 == 0:
                print("can't module by 0")
                return None
            else:
                return modulus(n1, n2)

def add(n1, n2):
    return n1 + n2

def minus(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def modulus(n1, n2):
    return n1 % n2


main()