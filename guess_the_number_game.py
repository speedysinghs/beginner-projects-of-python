# guess the number
import random
random_choice = random.randint(1,20)
livesLeft = 5
while(True):
    userInput = int(input("Enter number between 1 to 20: "))
    if userInput != random_choice:
        livesLeft = livesLeft - 1
        print(f"You have {livesLeft} lives left.")
        if userInput > random_choice:
            print("The random number is lower than your number")
        else:
            print("The random number is greater than your number")

    if userInput == random_choice:
        print("Congratulations !! you Won.")
        print(f"Total lives left {livesLeft}")
        break
    if livesLeft==0:
        print("Game over. You lose")
        print(f"The random number is {random_choice}")
        break

print(random_choice)