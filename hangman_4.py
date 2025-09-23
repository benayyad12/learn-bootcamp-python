import random 

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
#  Set 'lives' to equal 6.


# TODO-2: - If guess is not a letter in the chosen_word, Then reduce 'lives' by 1.
    #  If lives goes down to 0 then the game should stop and it should print "You lose."


# TODO-3: - print the ASCII art from 'stages'
    #  that corresponds to the current number of 'lives' the user has remaining.


word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

word_length=len(chosen_word)
placeholder=""
for i in range(word_length):
    placeholder+="_"
print(placeholder)

game_over=False
correct_word=[]
lives=6

while not game_over:
    guess=input("Guess a letter:\n").lower()
    display=""
    for letter in chosen_word:
        if guess == letter:
            display+=letter
            correct_word.append(letter)
        elif letter in correct_word:
            display+=letter
        else:
            display+="_"
    
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            print("You lose")
            game_over=True

    if "_" not in display:
        print("You win!")
        game_over=True

    print(stages[lives])
