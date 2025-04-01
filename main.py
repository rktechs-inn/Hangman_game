import random
import hangman_words
import hangman_art # you can also use "from hangman_art import stages"

lives = 6
game_over = False
correct_letters = []

#Imported the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)
print("\n<--- You have "'6'" lives to win this game --->\n")

#To print empty spaces using "_"
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

#main loop
while not game_over:
    #Code below to tell the user how many lives they have left.
    # print("You have " +str(lives)+ " lives left\n")
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print("You have already guessed the letter: " + guess)

    display = "" #to store guessed letter and display it with remaining "_"

    for letter in chosen_word:
        if letter == guess:
            display += letter
            print("You guessed the right letter\n")
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display+ "\n")

    #what if you win or lose
    if "_" not in display:
        game_over = True
        print("You won the game! Perfectly guessed")
    elif guess not in chosen_word:
        lives -=1
        print(f"Wrong guess! '" +guess+ "' is not in the word. You lose a life")
        print(hangman_art.stages[lives])
        print("You have " + str(lives) + " lives left\n")
        if lives == 0:
            game_over = True
            print("Game Over! You hung")
            print("The word was: " +chosen_word)
