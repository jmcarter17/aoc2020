from utils import timer
import numpy as np


@timer
def main():
    with open("inputs/day13.txt") as f:
        data = [ln.strip() for ln in f]

    data[0] = int(data[0])
    data[1] = [int(i) if i != "x" else None for i in data[1].split(",")]

    print(solve_day13(data))


@timer
def solve_day13(data):
    result1 = part1(data)
    result2 = part2(data[1])

    return result1, result2


@timer
def part1(data):
    goal = data[0]
    data = [i for i in data[1] if i]

    mods = [x - goal % x for x in data]
    idx = mods.index(min(mods))

    return mods[idx] * data[idx]


@timer
def part2(data):
    data = [(d, idx) for idx, d in enumerate(data) if d]
    guess, skip = data[0][0], data[0][0]
    idx = 1
    total_len = len(data)
    while idx < total_len:
        x, i = data[idx]
        while (guess + i) % x != 0:
            guess += skip
        skip = np.lcm(skip, data[idx][0])
        idx += 1

    return guess


def test_part2():
    with open("inputs/day13test2.txt") as f:
        data = [ln.strip() for ln in f]

    data = [[int(i) if i != "x" else None for i in ln.split(",")] for ln in data]
    for i in data:
        print(part2(i))

    print(part2([1789, 37, 47, 1889]))


if __name__ == "__main__":
    main()
    # test_part2()
