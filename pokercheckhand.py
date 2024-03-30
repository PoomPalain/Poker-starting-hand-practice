def evaluate_hand(hand):
    # Define your categories here
    playable = {'A-A', 'K-K', 'Q-Q', 'J-J', '10-10', '9-9', '8-8', '7-7', 'A-K', 'A-Q', 'A-J', 'A-10', 'K-Q', 'K-J', 'K-10', 'Q-J', 'Q-10', 'J-10', 'J-9', '10-9'}
    playable_till_flop = {'6-6', '5-5', 'A-9', 'A-8', 'A-7', 'A-6', 'K-9', 'Q-9', 'Q-8', 'J-8', '10-8', '9-8'}
    playable_till_raise = {'4-4', '3-3', '2-2', 'A-5', 'A-4', 'A-3', 'A-2', 'K-8', 'K-7', 'K-6', 'K-5', 'K-4', 'K-3', 'K-2', 'J-7', '10-7', '9-7', '9-6', '8-7', '8-6', '7-6', '7-5', '6-5', '5-4'}

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
    while True:
        user_input = input("Enter a starting hand (e.g., 2-3), or type 'end' to quit: ").upper()
        if user_input == "end":
            break
        result = evaluate_hand(user_input)
        print(f"Result: {result}")

if __name__ == "__main__":
    main()
