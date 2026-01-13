number = 67

print(".......Welcome to the Guess the numebr game.......")

print("You have to guess the number to win this game Let's Begin................")

count = 0
while(True):
    guess = int(input("Enter your guess number: "))
    count = count + 1

    # diff = abs(guess - number)

    if guess == number:
        print("You guess the RIGHT NUMBER. YOU WON")
        break
    elif(guess < 40 or guess > 85):
        print("GUESS AGIAN")
    elif(guess < 55 ):
        print("GO HIGHER, Try Again!")
    elif(guess > 80):
        print("GO LOWER, Try Again!")

    elif(guess < 67 and guess >= 60 or guess > 67 and guess < 72):
        print("Too close, Try Again!")

    elif(guess < 60 and guess > 55 or guess >= 72 and guess <= 80):
        print("You are going closer, Try Again!")
    


if count == 1: 
    print("You guessed the number in first try")
else:
    print(f"You guessed the number in {count} tries")

