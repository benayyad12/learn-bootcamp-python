import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

guess = input("Guess a letter:\n").lower()
print(guess)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

word_length = len(chosen_word)
placeholder=""

for i in range(word_length):
     placeholder+="_"

print(placeholder)

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display=""
for letter in chosen_word:
     if guess == letter:
          display+=guess
     else:
          display+="_"

print(display)
          
