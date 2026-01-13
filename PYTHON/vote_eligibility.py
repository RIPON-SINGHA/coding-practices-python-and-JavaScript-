def main():
    age = int(input("what is your age? "))
    
    # result = can_vote(age)
    # if result:
    #     print(result)

    print(can_vote(age))


def can_vote(age):
    if age <= 0:
        return "Enter a valid age!"
    elif age < 18:
        # print("Your are not eligible for voting right now!")

        return "Non-Eligible"
    else:
        # print("your are eligible for voting!")

        return "eligible"

main()