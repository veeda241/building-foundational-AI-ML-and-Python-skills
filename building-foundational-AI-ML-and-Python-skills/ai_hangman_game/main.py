from ai_brain import guess_letter
from utils import update_word_state, display_word

# Initialize game
print("🤖 Welcome to AI Hangman!")
word_length = int(input("Enter your word length: "))
current_state = ['_'] * word_length
used_letters = []
wrong_guesses = 0
max_guesses = 6

while wrong_guesses < max_guesses and '_' in current_state:
    letter = guess_letter(used_letters)
    print(f"\nAI guesses: '{letter}'")
    response = input("Enter positions (e.g. 1,3) or 'n': ").strip().lower()

    if response == 'n':
        wrong_guesses += 1
        print(f"❌ Wrong guess! {max_guesses - wrong_guesses} tries left.")
    else:
        positions = [int(i.strip()) - 1 for i in response.split(',')]
        current_state = update_word_state(current_state, letter, positions)

    used_letters.append(letter)
    display_word(current_state)

# Final output
if '_' not in current_state:
    print("🎉 AI guessed the word:", ''.join(current_state))
else:
    print("😵 AI lost! Final state:", ''.join(current_state))
