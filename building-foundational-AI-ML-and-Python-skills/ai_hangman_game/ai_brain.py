# ai_brain.py
# Handles AI's smart letter guessing based on frequency

letter_frequency = 'etaoinshrdlucmfwypvbgkjqxz'

def guess_letter(used_letters):
    for letter in letter_frequency:
        if letter not in used_letters:
            return letter
