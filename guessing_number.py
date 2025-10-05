import random



def guessing_game():
    print( r""" ________                            .__                   ________                       
 /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ """)
  
    print("Welcome to the number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    level = {
        'easy': 10,
        'hard': 5
    }
    number = random.randint(1,100)
    attempts = 0
    while attempts < level[difficulty]:
        print(f"You have {level[difficulty]-attempts} attempts remaining to guess the right number")
        guess = int(input("Make a guess: "))
        if guess < number:
            print("Too low")
            print("Guess Again.")
        elif guess > number:
            print("Too high")
            print("Guess Again.")
        else:
            print(f"Congratulations you guessed the right number in {attempts} attempts")
        attempts+=1
    print(f"You run out of attempts, the number was {number}")


guessing_game()
