import random

# Define the ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] # suit make you ~8% more winning rate which will be see in the flop so doesnt matter for me.

def generate_starting_hand():
    card1 = random.choice(ranks)
    card2 = random.choice(ranks)
    return card1, card2

def evaluate_hand(hand):
    # Define your categories here
    playable = {'A-A', 'K-K', 'Q-Q', 'J-J', '10-10', '9-9', '8-8', '7-7', 'A-K', 'A-Q', 'A-J', 'A-10', 'K-Q', 'K-J', 'K-10', 'Q-J', 'Q-10', 'J-10', 'J-9', '10-9'}
    playable_till_flop = {'6-6', '5-5', 'A-9', 'A-8', 'A-7', 'A-6', 'K-9', 'Q-9', 'Q-8', 'J-8', '10-8', '9-8'}
    playable_till_raise = {'4-4', '3-3', '2-2', 'A-5', 'A-4', 'A-3', 'A-2', 'K-8', 'K-7', 'K-6', 'K-5', 'K-4', 'K-3', 'K-2', 'J-7', '10-7', '9-7', '9-6', '8-7', '8-6', '7-6', '7-5', '6-5', '5-4'}
    #else is losing hand

    # Create both combinations of the cards
    card1, card2 = hand.split('-')
    normalized_hand1 = f"{card1}-{card2}"
    normalized_hand2 = f"{card2}-{card1}"

    return (
        "p" if normalized_hand1 in playable or normalized_hand2 in playable
        else "f" if normalized_hand1 in playable_till_flop or normalized_hand2 in playable_till_flop
        else "r" if normalized_hand1 in playable_till_raise or normalized_hand2 in playable_till_raise
        else "l"
    )

def main():
    print("Welcome to the Poker Starting Hand Guessing Game!")
    print("Type 'end' to quit.")

    correct_guesses = 0
    total_guesses = 0

    while True:
        card1, card2 = generate_starting_hand()
        print(f"Your starting hand: {card1}, {card2}")
        guess = input("Is it playable(p), playable_till_flop(f), playable_till_raise(r) or lose(l) ? ").lower()  # Convert input to lowercase

        if guess == "end":
            break

        actual_category = evaluate_hand(f"{card1}-{card2}")
        if guess in ['p', 'f', 'r', 'l']:
            if guess == actual_category:
                print("Correct!")
                correct_guesses += 1
            else:
                print(f"Wrong! It's actually {actual_category}.")
            total_guesses += 1
        else:
            print("Invalid input. Please enter one of the specified characters.")

    accuracy = (correct_guesses / total_guesses) * 100 if total_guesses != 0 else 0  # Handle division by zero
    print(f"Game over! Your accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()

source = "https://depositwet.medium.com/texas-holdem-conservative-strategy-c35826e67394"
