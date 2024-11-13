HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

count = 8
wrong_guess = 0
word = "yigit"
correct_guesses = set()
display_word = ["_"] * len(word)  # List to show the word with blanks

while count > 0:
    print("Current word:", " ".join(display_word))  # Show the current state of the word
    guess = input("Guess a letter(Type 1 for quit.): ").strip().lower()

    if guess == "1":
        print("Quitting from game...")
        break

    if len(guess) != 1:  # Ensure the input is a single letter
        print("Please enter a single letter.")
        continue

    if guess in word:
        if guess not in correct_guesses:  # Avoid duplicate correct guesses
            correct_guesses.add(guess)
            print("You guessed correctly!")

            # Update display_word with the guessed letter in the correct positions
            for index, letter in enumerate(word):
                if letter == guess:
                    display_word[index] = guess

        else:
            print("You've already guessed that letter.")

        # Check if all letters have been guessed
        if "_" not in display_word:
            print("Congratulations! You've guessed the word:", word)
            break  # Exit the loop since the user has won
    else:
        print(HANGMANPICS[wrong_guess])
        count -= 1
        wrong_guess += 1
        print("You guessed wrong. You have", count, "guesses left.")

if count == 0:
    print("Game over! You lose.")
    print("The word was:", word)