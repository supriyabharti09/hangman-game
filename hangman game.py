import random

# List of words to choose from
words = ["python", "hangman", "programming", "developer", "computer", "keyboard", "algorithm"]
chosen_word = random.choice(words)
display = ["_"] * len(chosen_word)
lives = 6
guessed_letters = []

# Game loop
while lives > 0 and "_" in display:
    print("\nCurrent word: " + " ".join(display))
    print(f"Lives remaining: {lives}")
    print(f"Guessed letters: {', '.join(guessed_letters)}")

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
        print("Good guess!")
    else:
        lives -= 1
        print(f"Wrong guess! '{guess}' is not in the word.")

if "_" not in display:
    print("\nCongratulations! You've guessed the word:", chosen_word)
else:
    print("\nGame Over! The word was:", chosen_word)
