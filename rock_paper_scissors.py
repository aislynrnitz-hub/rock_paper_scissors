#imports random to allow the computer to randomly choose rock, paper, or scissors.
import random

#sets my counts variables count to 0 so that they can be used and incremented later.
user_win_count = 0
computer_win_count = 0
good_rounds = 0

#This function gets the user's choice of rock, paper, or scissors and makes sure the input is valid.
#it also converts the inputted answer to lowercase so that it can be compared to the computer's choice.
def get_player_choice():
    user_answer = input("Enter rock, paper, scissors: ").lower()
    while user_answer != "rock" and user_answer != "paper" and user_answer != "scissors":
        print(f"Sorry, {user_answer} is not a valid choice. Please try again.")
        user_answer = input("Enter rock, paper, scissors: ").lower()
    return user_answer

#determines the winner of each round based on the user and computer choices. Returns whether the user won, lost, or tied.
def determine_winner(user_answer, computer_answer):
    if user_answer == computer_answer:
        return "Tie! play again."
    elif user_answer == "rock" and computer_answer == "scissors":
        return "You won!"
    elif user_answer == "paper" and computer_answer == "rock":
        return "You won!"
    elif user_answer == "scissors" and computer_answer == "paper":
        return "You won!"
    else:
        return "You lose!"

#allows the user to input the number of rounds they want to play, and makes sure the number is odd
print("Welcome to Rock, Paper, Scissors!")
rounds = int(input("How many rounds would you like to play? "))
while rounds % 2 == 0:
    print("Sorry, the number must be an odd number")
    rounds = int(input("How many rounds would you like to play? "))

#runs the game until the times someone wins matches the inputted number. It also keeps track of the score
#and prints the the computer choice and the result of each round.
while good_rounds < rounds:
    user_answer = get_player_choice()
    computer_answer = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_answer}")
    result = determine_winner(user_answer, computer_answer)
    print(result)
    if result == "You won!":
        user_win_count += 1
        good_rounds += 1
    elif result == "You lose!":
        computer_win_count += 1
        good_rounds += 1

#Prints the final score and lets the user know if they won or lost the overall game.
print(f"\nScore: -- You: {user_win_count} | Computer: {computer_win_count}")
if user_win_count > computer_win_count:
    print("You win!!!\nThanks for playing!")
else:
    print("You lose!\nThanks for playing!")