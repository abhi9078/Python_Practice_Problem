import random


def gambler(stake, goal):
    """
    function for gambler problem
    :param stake: the amount that user have
    :param goal: the goal amount
    :return: number of wins and result
    """
    win_count = 0
    if stake <= 0:
        print("player didn't have any money ")
    else:
        while 0 < stake < goal:
            check = random.randint(0, 1)
            if check == 0:
                stake += 1
                win_count += 1
            else:
                stake -= 1
        if stake <= 0:
            print("player goes broke")
        else:
            print("player rich goal")
        return win_count


if __name__ == "__main__":
    stake_input = int(input("Please enter stake amount"))
    goal_input = int(input("Please enter goal amount"))
    result = gambler(stake_input, goal_input)
    print("Number of time player win while betting is: ", result)


