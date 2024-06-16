'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("Welcome to Rock, Paper, Scissors!")
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("You lose!")
