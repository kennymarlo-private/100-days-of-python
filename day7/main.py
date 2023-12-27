import random
from hangman_art import logo, stages
from hangman_words import word_list

print(logo)

end_of_game = False
chosen_word = random.choice(word_list)
lives = 6

# display empty
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # clear()

    if guess in display:
        print(f"You already guess letter \'{guess}\'")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"The letter \'{guess}\', is not in word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print(f"The chosen word is {chosen_word}")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You won!")

    print(stages[lives])
