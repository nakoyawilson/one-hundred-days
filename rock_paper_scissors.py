import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice_list = [rock, paper, scissors]
print("Welcome to Rock Paper Scissors")
print("The rules to play are pretty simple.")
print("The player and the computer each choose a number that will represent the elements of the game: rock, paper and scissors.")
print("The outcome of the game is determined by 3 simple rules:")
print("\t- Rock wins against scissors.")
print("\t- Scissors win against paper.")
print("\t- Paper wins against rock.")
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(choice_list[player_choice])
computer_choice = random.randint(0,2)
print("Computer chose:")
print(choice_list[computer_choice])
if player_choice == computer_choice:
    print("It's a tie.")
if (player_choice == 0 and computer_choice == 2) or (player_choice == 2 and computer_choice == 1) or (player_choice == 1 and computer_choice == 0):
    print("You win!")
else:
    print("You lose.")