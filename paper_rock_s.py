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

choices = [rock, paper, scissors]

computer_choice = random.randint(0,2)
user_choice = int(input("Choose 0: Rock , 1: Paper and 2: Scissors\n"))
if user_choice not in [0,1,2]:
    user_choice = int(input("Choose a valid option =>  0: Rock , 1: Paper and 2: Scissors\n"))

print(f"The computer choosed:\n {choices[computer_choice]}")
print("\n\n")
print(f"The user choosed:\n {choices[user_choice]}")

if computer_choice == user_choice:
    print("It's a draw")
elif ((user_choice == 2 and computer_choice == 1) or (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0)):
    print("You win!")
else:
    print("You lost!")