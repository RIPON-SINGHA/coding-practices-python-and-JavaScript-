def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("select an operator (+, -, /, *): ")
    result = calculate(num1, num2, operator)
    print(f"{num1} {operator} {num2} = {result}")


def calculate(num1, num2, operator):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if(num2 == 0):
                print("Can not divide by zero!")
                return None
            else:
                return num1 / num2
        case _:
            print("invalid Input operator!")
            return None
    


main()