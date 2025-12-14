import random

user_history = {"rock": 0, "paper": 0, "scissors": 0}

def ai_choice():
    if sum(user_history.values()) == 0:
        return random.choice(list(user_history.keys()))

    predicted = max(user_history, key=user_history.get)

    if predicted == "rock":
        return "paper"
    elif predicted == "paper":
        return "scissors"
    else:
        return "rock"

user = input("Enter rock, paper, or scissors: ").lower()
user_history[user] += 1

computer = ai_choice()

print("Computer chose:", computer)

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins!")
