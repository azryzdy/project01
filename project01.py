import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif user_action == Action.Rock:
        if computer_action == Action.Scissors:
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action == Action.Paper:
        if computer_action == Action.Rock:
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == Action.Scissors:
        if computer_action == Action.Paper:
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action
while True:
    try:
        user_action = get_user_selection()
    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}]"
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue

    computer_action = get_computer_selection()
    determine_winner(user_action, computer_action)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

 

"""
while True:
    value = input("Rock, paper, scissor : ")
    game = ["rock", "paper", "scissor"]
    bot = random.choice(game)
    print("You choose ", value, "While computer choose ", bot)

    if value == bot:
        print("It's a tie")
    elif value == "rock":
        if bot == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif value == "paper":
        if bot == "rock":
            print("You win")
        else:
            print("You lose")
    elif value == "scissor":
        if bot == "paper":
            print("You win")
        else:
            print("You lose!")
    else:
        print("Wrong input")
    lol = input("You want to continue? y/n: ")
    if lol.lower() != "y":
        break
"""

"""
for value in range(1,value):
    if(value == 1 >= gametest):
        print("Your tied!")
    elif(value == 2 >= gametest):
        print("You suck!")
    elif(value == 3 >= gametest):
        print("You win!")
    value = input("Rock - 1 paper - 2 scissor - 3 : ")
    gametest = random.randint(1,3)
    print("\n", gametest)



value = input("Enter value: ")
for value in range(1,5):
    print("hello world")
    value = input("Enter value: ")
"""