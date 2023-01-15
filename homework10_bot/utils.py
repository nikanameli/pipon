import random


def random_stones():
    return random.randint(60, 120)


def make_turn(stones):
    if stones <= 13:
        return stones
    ost = stones % 14
    if not ost:
        return random.randint(1, 13)
    return ost


def robot_first(stones):
    return stones % 14 == 0