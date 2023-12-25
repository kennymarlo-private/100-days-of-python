import random

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissor
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))


if user_choice >= 3 or user_choice < 0:
    print("You type an invalid number, you lose!")
else:
    game_images = [rock, paper, scissors]
    computer_choice = random.randint(0, 2)
    if (user_choice == 0 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1) or (
            user_choice == 1 and computer_choice == 0):
        print("You choose: \n")
        print(game_images[user_choice])
        print("Computer choose: \n")
        print(game_images[computer_choice])
        print("You won!")
    elif user_choice == computer_choice:
        print("You choose: \n")
        print(game_images[user_choice])
        print("Computer choose: \n")
        print(game_images[computer_choice])
        print("It\'s a draw!")
    else:
        print("You choose: \n")
        print(game_images[user_choice])
        print("Computer choose: \n")
        print(game_images[computer_choice])
        print("You lose!")
