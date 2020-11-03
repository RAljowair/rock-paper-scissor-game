import random # importing random library
import time # importing time library

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
tools = {1: "Rock", 2: "Paper", 3: "Scissors"}


# to make messages take 1s per message
def print_pulse(string):
    time.sleep(1)
    print(string)
    

def winning_message():
    print_pulse("\nWinner Winner Chicken Dinner :)")
    print_pulse("Congrats!")


def losing_message():
    print_pulse("\nDefeted :(")
    print_pulse("Better luck next time ;)")


# game introduction message and taking the player's name 
def start_message():
    print_pulse("Hello")
    print_pulse("Welcome to Rock, Paper, Scissors game :)")
    # Checking if there is a numbers or symbols
    while True:
        try:
            player_name = str(input("First what's Your name: "))
            if any(char.isdigit() for char in player_name) or any(char.isalnum() for char in player_name):
                raise Exception
            else:
                break
        except:
            print("Your name should be only letters!")
    print_pulse("Hello " + player_name)


# to select choices form the user and computer
def choices():
    print_pulse("Choose the number of which tool you want:")
    print_pulse("1.Rock")
    print_pulse("2.Paper")
    print_pulse("3.Scissors")
    while True:
        try:
            player_response = int(input(">"))
            if player_response > 3 or player_response < 1:
                print("You must enter one of these numbers [1, 2, 3]:")
            else:
                break
        except:
                print("You must enter Only Numbers try again:")
    player_choice = tools[player_response]
    print_pulse(f"Your choice is: {player_choice}")
    random_num = random.randint(1, 3)
    computer_choice = tools[random_num] 
    print_pulse(f"Computer choice is: {computer_choice}")


    # to compare tools and who will win
    def compare_choices():
        if player_choice.lower() == "rock" and computer_choice.lower() == "paper":
            losing_message()
        elif player_choice.lower() == "rock" and computer_choice.lower() == "scissors":
            winning_message()
        elif player_choice.lower() == "paper" and computer_choice.lower() == "rock":
            winning_message()
        elif player_choice.lower() == "paper" and computer_choice.lower() == "scissors":
            losing_message()
        elif player_choice.lower() == "scissors" and computer_choice.lower() == "rock":
            losing_message()
        elif player_choice.lower() == "scissors" and computer_choice.lower() == "paper":
            winning_message()
        elif player_choice.lower() == computer_choice.lower():
            print_pulse("\nDRAW!!!")
    compare_choices()


def game():
    start_message()
    choices()


game()
