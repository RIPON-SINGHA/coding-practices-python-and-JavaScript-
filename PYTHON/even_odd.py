# WE CAN DO SUCH LOGIC LIKE THIS IMPLIMENTATION
def main():
    number = int(input("Enter your number: "))
    if Even_Odd(number):
        print(f"Ypur number {number} is Even")
    else:
        print(f"Your number {number} is Odd")


def Even_Odd(num):
    return True if num % 2 == 0 else False

main()



# ANOTHER SIMPLE WAY TO DO THAT:
def evenOdd():
    number = int(input("Enter your number: "))
    if number % 2 == 0:
        print(f"Ypur number {number} is Even")
    else:
        print(f"Your number {number} is Odd")


evenOdd()