# Asking for a number input until user gives a valid input
def safeIntInpt():

    while True:
        try:
            number = int(input("Enter a number: "))
            if number > 0:
                return number
            else:
                print("Enter a positive integer number")
        except ValueError:
            print("Enter a valid number!")

print(safeIntInpt())