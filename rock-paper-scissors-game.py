import random # importing random library
import time # importing time library


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


# game intro 
def start_message():
    print_pulse("Hello")
    print_pulse("Welcome to Rock, Paper, Scissors game :)")
    try:
        player_name = str(input("First what's Your name: "))
    except:
        print("Your name should be only letters!")
    print_pulse("Helllooo " + player_name)


# to select chices form the user and computer
def choices():
    print_pulse("Choose the number of which tool you want:")
    print_pulse("1.Rock")
    print_pulse("2.Paper")
    print_pulse("3.Scissors")
    print_pulse("-> ")
    while True:
        try:
            player_response = int(input())
            break
        except:
            if player_response > 3 or player_response < 1:
                raise print_pulse("You mmust enter one of the three numbers above!") 
            print("You must enter Only Numbers")

    player_choice = tools[player_response]
    print_pulse(f"Your choice is: {player_choice}")
    random_num = random.randint(1, 3)
    computer_choice = tools[random_num] 
    print_pulse(f"Computer choice is: {computer_choice}")
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
        

start_message()
choices()