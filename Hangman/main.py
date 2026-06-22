import random

def hangman():
    # 1. Difficulty levels
    word_bank = {
        "easy": ["hello", "mango", "apple", "pizza"],
        "medium": ["python", "coding", "random", "function"],
        "hard": ["algorithm", "database", "machinelearning", "fastapi"]
    }

    level = input("Choose difficulty - easy/medium/hard: ").lower()
    if level not in word_bank:
        level = "easy"
        print("Invalid choice, defaulting to easy")

    word = random.choice(word_bank[level])
    correct_word = ["_"] * len(word)
    lives = {"easy": 10, "medium": 8, "hard": 6}[level]

    guessed_letters = []
    score = 0

    print(f"\n=== Hangman Game - {level.upper()} Mode ===")
    print(f"Lives: {lives} | Word length: {len(word)}")
    print("Word:", " ".join(correct_word))

    '''Main game loop'''
    while lives > 0:
        guess = input("\nEnter a letter or 'quit' to exit: ").lower()

        if guess == 'quit':
            print(f"Game over! Word was: {word}")
            return

        '''Input validation'''
        if len(guess)!= 1 or not guess.isalpha():
            print("Ek letter daal a-z tak!")
            continue

        if guess in guessed_letters:
            print(f"Pehle hi '{guess}' try kar chuka hai!")
            continue

        guessed_letters.append(guess)
        found = False

        '''to check letter'''
        
        for i in range(len(word)):
            if guess == word[i]:
                correct_word[i] = guess
                found = True
                score += 10

        '''print result'''
        if found:
            print("✅ Correct!")
            if "_" not in correct_word:
                score += lives * 5 # bonus for remaining lives
                print(f"\n You won! Word: {word}")
                print(f"Final Score: {score}")
                return
        else:
            lives -= 1
            print(f"Wrong! {lives} lives left")

        print("Word:", " ".join(correct_word))
        print(f"Guessed: {', '.join(sorted(guessed_letters))}")

    print(f"\n You lose! The correct word was: {word}")
    print(f"Final Score: {score}")

# Replay option
while True:
    hangman()
    play_again = input("\nDo you want to play again? y/n: ").lower()
    if play_again!= 'y':
        print("Thanks for playing! Bye 👋")
        break
