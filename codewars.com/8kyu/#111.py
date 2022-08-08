# You get any card as an argument. Your task is to return the suit of this card (in lowercase).

def define_suit(card):
    if card[-1].lower() == 'c':
        return 'clubs'
    elif card[-1].lower() == 'd':
        return 'diamonds'
    elif card[-1].lower() == 'h':
        return 'hearts'
    elif card[-1].lower() == 's':
        return 'spades'
    print(card)


print(define_suit('3C'))
