def main():
    age = int(input("what's you current age? "))
    ageCal(age)


def ageCal(age):
    if age < 0:
        print("Age must be in positive!")
    else:
        print(f"5 years later you will be {age + 5} years old.")

main()