import pytest


def vending_machine(amount):
    """
    function for vending machine program
    :param amount: actual amount
    :return: change in different note
    """
    notes = [1000, 500, 100, 50, 10, 5, 2, 1]
    note_counter = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    note_count = []

    for i, j in zip(notes, note_counter):
        if amount >= i:
            j = amount // i
            note_count.append(j)
            amount = amount - j * i
            print(i, " : ", j)

    total = sum(note_count)
    return total


def test_my_func():
    assert vending_machine(235) == 6


if __name__ == "__main__":
    print("Change notes given by Vending machine is: ")
    output = vending_machine(235)
    print("Number of notes are: ", output)
