import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
          guess = int(input(f'Guess a number between 1 and {x}:'))
          if guess <  random_number:
               print('sorry,guess again. Too low.')
          elif guess > random_number:
               print('Sorry, guess again. Too high.')

    print(f'yay,congrats. you have guessed the number {random_number} correctly')


def computer_guess(x):
     low = 1
     high = x
     feedback = ''
     while feedback != 'c':
          if low != high:
             guess = random.randint(low, high)
          else:
               guess = low
          print("choose a number in mind")
          feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??').lower() 
          if feedback == 'h':
               high = guess - 1
          elif feedback == 'l':
               low = guess + 1

     print(f'yay! The computer guessed your number,{guess}, correctly!')     

print("------------WELCOME TO GUESS THE NUMBER GAME----------")
print("select option")
print("1.Guess by computer\n2.Guess by user")
option = int(input())
if option == 1:
  computer_guess(10)
elif option == 2:
  guess(10)
