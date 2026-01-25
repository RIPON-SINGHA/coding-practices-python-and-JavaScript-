# creating number guessing game 
import random

num = random.randint(1, 51) 
count = 0

while True:
    try:
        guessNum = int(input("Enter your guess number (1 - 50)): ")) # 87
    except ValueError:
        print("Enter a valid positive integer number")
        continue

    count = count + 1     
    diff = guessNum - num
    dist = abs(diff)

    if diff == 0:
        if count == 1:
            print(f"YOU HAVE GUESSED THE RIGHT NUMBER IN YOUR FIRST TRY")
            break
        else:
            print(f"You have guessed the right number in {count} tries")
            break
        
    elif dist <= 10:
        print("Go Up" if diff < 0 else "Go Down")
    elif dist <= 20:
        print("Too low" if diff < 0 else "Too High")
    else:
        print("Way too small" if diff < 0 else "Way too Large")