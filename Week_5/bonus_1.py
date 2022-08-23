from random import randrange


def create_deck():
    """
    creates a deck of cards
    :return: list of cards
    """
    cards_deck = []

    for suit in ["s", "h", "d", "c"]:
        for value in ["2", "3", "4", "5", "6", "7", "8", "9",
                      "T", "J", "Q", "K", "A"]:
            cards_deck.append(value + suit)
    return cards_deck


def shuffle(cards_to_shuffle):
    """
    shuffles the deck of cards
    :param cards_to_shuffle: list[str]
    :return: None
    """
    for i in range(0, len(cards_to_shuffle)):
        other_pos = randrange(i, len(cards_to_shuffle))
        temp = cards_to_shuffle[i]
        cards_to_shuffle[i] = cards_to_shuffle[other_pos]
        cards_to_shuffle[other_pos] = temp


if __name__ == '__main__':
    cards = create_deck()
    print("The original deck of cards is:")
    print(cards)

    shuffle(cards)
    print("The shuffled deck of cards is: ")
    print(cards)
