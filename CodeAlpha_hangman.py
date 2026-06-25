import random

words = ["python", "keyboard", "matrix", "algorithm", "compiler"]
word = random.choice(words)

guessed = []
lives = 6

print("\n🎮 HANGMAN  |  6 lives  |  Guess the word!\n")

while lives > 0:
    # Show current word state
    display = "  ".join(letter if letter in guessed else "_" for letter in word)
    print(f"Word:   {display}")
    print(f"Lives:  {'❤️ ' * lives}{'🖤 ' * (6 - lives)}")

    if all(letter in guessed for letter in word):
        print(f"\n🎉 YOU GOT IT! The word was '{word}'. Legend!\n")
        break

    if guessed:
        print(f"Tried:  {', '.join(sorted(guessed))}")

    guess = input("\nYour guess: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️  One letter at a time!\n")
        continue

    if guess in guessed:
        print("🔁 Already tried that one!\n")
        continue

    guessed.append(guess)

    if guess in word:
        print("✅ Yes!\n")
    else:
        lives -= 1
        print(f"❌ Nope! -{1} life\n")

else:
    print(f"💀 Out of lives! The word was '{word}'. Better luck next time!\n")
