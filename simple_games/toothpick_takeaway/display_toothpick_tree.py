def display_turn_tree(cards_left, player, cards_taken, turn):
    """
    Displays a tree of all possible turns for Toothpick Takeaway

    Args:
        cards_left  (int) : The number of cards left on the table AFTER the turn
        player:     (int) : The player who just picked up cards
        cards_taken (int) : How many cards the player picked up
        turn:       (int) : Which turn of the match it is

    Returns:
        N/A
    """

    # Indent the line relative to what turn of the match it is
    for _ in range(turn):
        print(end="    ")

    # Print out the formatted string of the player and game state
    print("P{}-{}: ({})".format(player, cards_taken, cards_left))

    # If no more cards are left, return
    if cards_left == 0:
        return

    # Else, increase the turn counter and change the player
    turn += 1
    next_player = ((player) % 2) + 1

    # Recurse if player takes 1 card
    display_turn_tree(cards_left - 1, next_player, 1, turn)
    # Recurse if player takes 2 cards (only possible if there are at least 2 cards left)
    if cards_left > 1:
        display_turn_tree(cards_left - 2, next_player, 2, turn)


num_cards = int(input("How many cards are being played? "))
player = 1
cards_taken = int(input("How many cards will player 1 take? (1 or 2): "))
turn = 0
display_turn_tree(num_cards - cards_taken, player, cards_taken, turn)
print("Format: P[player]-[cards taken]: ([cards left])")
