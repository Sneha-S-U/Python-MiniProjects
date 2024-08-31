import random


def play():
    user_score = 0
    computer_score = 0
    max_score = 3

    print("Welcome to Rock Paper Scissors!")

    while True:
        user = input("what's your choice \n 'r' for rock,'p' for paper, 's' for scissors (or type 'quit' to exit)\n")
        if user == 'r':
            print("you choose rock.")
        elif user == 'p':
            print("you choose paper.")
        elif user == 's':
            print("you chose scissors.")
        elif user == 'quit':
            print("Thanks for playing!")
            break 
        elif user not in ['r', 'p', 's']:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        computer = random.choice(['r', 'p', 's'])

        if computer == 'r':
            print("Computer choose rock.")
        elif computer == 'p':
            print("Computer choose paper.")
        elif computer == 's':
            print("Computer chose scissors.")
        
        result = is_win(user, computer)
        
        if result == 'win':
            print("You win!\n")
            user_score += 1
        elif result == 'lose':
            print("You lose!\n")
            computer_score += 1
        else:
            print("It's a tie!\n")
        
        print_score(user_score, computer_score)

        if user_score == max_score or computer_score == max_score:
            if user_score > computer_score:
                print("Congratulations! You won the game!")
            else:
                print("Game over! The computer won the game!")
            break
       
        
def is_win(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
         return 'win'
    else:
         return 'lose'
    

    
def print_score(user_score, computer_score):
    print(f"Score: You {user_score} - {computer_score} Computer\n")


print(play())