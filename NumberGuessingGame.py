
print("Number guessing game")
number = 7
chances = 0
print("Guess a number (between 1 and 9):")

# while loop to count number of chances
while chances < 5:
    guess = int(input("Enter your guess:- "))

#Compare the user entered number with the number to be guessed
    if guess == number:
        print("Congratulation YOU WON!!!")
        break

    elif guess < number:
        print("Your guess was too low: Guess a number higher than", guess)

    else:
        print("Your guess was too high: Guess a number lower than", guess)

    chances+=1

#Check whether the user guessed the correct number
if not chances < 5:
    print("YOU LOSE!!! The number is", number)