import random

def word_guessing_game():
    words = ['banana', 'apple', 'orange', 'kiwi', 'strawberry', 'blueberry', 'watermelon', 'pineapple', 'grape']
    secret_word = random.choice(words).lower()
    attempts = 0
    max_attempts = 5
    guessed_letters = []

    print("Welcome to the Unique Word Guessing Game!")
    print("I've picked a secret word. Can you guess it?")

    while attempts < max_attempts:
        print("\nSecret Word: ", end="")
        for letter in secret_word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        
        print("\n")

        if len(guessed_letters) > 0:
            print("Guessed Letters:", ", ".join(guessed_letters))

        guess = input("Enter a letter or guess the whole word: ").lower()
        
        if guess == secret_word:
            print("Congratulations! You've guessed the secret word!")
            break
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter!")
            elif guess in secret_word:
                print("Good guess!")
                guessed_letters.append(guess)
            else:
                print("Try again!")
                guessed_letters.append(guess)
            attempts += 1
        else:
            print("Invalid input! Please enter a single letter or guess the whole word.")

    else:
        print("Sorry, you've run out of attempts. The secret word was:", secret_word)

if __name__ == "__main__":
    word_guessing_game()
