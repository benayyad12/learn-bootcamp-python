
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder=""
for i in range(len(chosen_word)):
    placeholder+="_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
correct_word=[]
game_over = False

while not game_over:
    guess = input("Guess a letter:\n").lower()

    display=""
    for letter in chosen_word:
        if guess == letter:
            display+=letter
            correct_word.append(letter)
        elif letter in correct_word:
            display+=letter
        else:
            display+="_"
    
    if "_" not in display:
        print("You win!")
        game_over=True




# TODO-2: Change the for loop so that you keep the previous correct letters in display.
