import itertools
import random

card_deck = list(itertools.product(range(1, 14), ["Spade", "Club", "Diamond", "Heart"]))
play1 = []
play2 = []
play3 = []


def player1():
    for i in range(100):
        random.shuffle(card_deck)
        join_ = card_deck[i][0], card_deck[i][1]
        if join_ not in play1:
            play1.append(join_)
        if len(play1) >= 13:
            break
    return play1


def player2():
    for j in range(100):
        random.shuffle(card_deck)
        join_ = card_deck[j][0], card_deck[j][1]
        if join_ not in play1 and join_ not in play2:
            play2.append(join_)
        if len(play2) >= 13:
            break
    return play2


def player3():
    for f in range(100):
        random.shuffle(card_deck)
        join_ = card_deck[f][0], card_deck[f][1]
        if join_ not in play1 and join_ not in play2 and join_ not in play3:
            play3.append(join_)
        if len(play3) >= 13:
            break
    return play3


if __name__ == "__main__":
    first = player1()
    second = player2()
    third = player3()

    print("Cards of first player is: ")
    print(first)
    print("Cards of second player is: ")
    print(second)
    print("Cards of third player is: ")
    print(third)
