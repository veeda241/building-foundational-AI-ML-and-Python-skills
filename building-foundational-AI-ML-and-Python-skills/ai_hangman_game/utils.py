def update_word_state(state, letter, positions):
    for pos in positions:
        if 0 <= pos < len(state):
            state[pos] = letter
    return state

def display_word(state):
    print("🔡 Current Word: ", ' '.join(state))
