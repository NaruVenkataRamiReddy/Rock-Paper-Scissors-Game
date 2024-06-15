#importing random module
import random
#Declaring available resourses
options = ["Rock", "Paper", "Scissors"]

#Selecting random option for machine
machine = random.choice(options)

#Declaring scores
user = False
machine_score = 0
user_score = 0

while True:
    user = input("Rock, Paper or  Scissors? ").capitalize()
    # Conditions of Rock, Paper and Scissors
    if user == machine:
        print("Tie!")
    elif user == "Rock":
        if machine == "Paper":
            print("You lose!", machine, "covers", user)
            machine_score+=1
        else:
            print("You win!", user, "smashes", machine)
            user_score+=1
    elif user == "Paper":
        if machine  == "Scissors":
            print("You lose!", machine, "cut", user)
            machine_score+=1
        else:
            print("You win!", user, "covers", machine)
            user_score+=1
    elif user == "Scissors":
        if machine == "Rock":
            print("You lose...", machine, "smashes", user)
            machine_score+=1
        else:
            print("You win!", user, "cut", machine)
            user_score+=1
    elif user =='End':
        print("Final Scores:")
        print(f"Computer's score is:{machine_score}")
        print(f"Your score is:{user_score}")
        break