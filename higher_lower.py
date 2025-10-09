import random
from game_data import data

logo=r"""
  ___ ___ .__       .__                   .____                               
 /   |   \|__| ____ |  |__   ___________  |    |    ______  _  __ ___________ 
/    ~    \  |/ ___\|  |  \_/ __ \_  __ \ |    |   /  _ \ \/ \/ // __ \_  __ \
\    Y    /  / /_/  >   Y  \  ___/|  | \/ |    |__(  <_> )     /\  ___/|  | \/
 \___|_  /|__\___  /|___|  /\___  >__|    |_______ \____/ \/\_/  \___  >__|   
       \/   /_____/      \/     \/                \/                 \/       
"""
vs=r"""
____   _____________
\   \ /   /   _____/
 \   Y   /\_____  \ 
  \     / /        \
   \___/ /_______  /
                 \/ 
"""

def generate_person():
    return random.choice(data)

# print(generate_person())

def format_person(person_,label):
    return f"{label}: {person_["name"]}, a {person_["description"]}, from {person_["country"]}"

person_A = generate_person()
person_B = generate_person()

# print(format_person(person_A,"Compare A"))
# print(format_person(person_A,"Against B"))
# choice = input("Who has more followers? Type 'A' or 'B': ").upper()

def compare_person(person_, person__, choice):
    if person_["follower_count"] > person__["follower_count"]:
          return choice == 'A'
    else:
         return choice == 'B'

# print(compare_person(person_A, person_B, choice))


game_is_over = False
score = 0
person_A = generate_person()
person_B = generate_person()

while not game_is_over:
        while person_A == person_B:
            person_A = generate_person()

        print(logo)
        print(format_person(person_A,"Compare A"))
        print(vs)
        print(format_person(person_B,"Against B"))

        choice = input("Who has more followers? Type 'A' or 'B': ").upper()
        if compare_person(person_A, person_B, choice):
             score = score + 1
             person_A = person_B
             print(f"You're right! Current score: {score}")
        else:
             print(logo)
             print(f"Sorry that's wrong. Final score: {score}")
             game_is_over=True

             

    
