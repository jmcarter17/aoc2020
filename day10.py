from collections import defaultdict
from functools import lru_cache
from itertools import groupby, combinations
from math import prod

from utils import timer


def is_necessary(data, idx):
    return idx <= 0 or idx >= len(data) - 1 or data[idx + 1] - data[idx - 1] != 2


#  This function only works for n = 1, 2, 3, 4.
#  For 5, this should return 24, I think, but this gives 25
#  In my input, the longest series of non-necessary items is 3, so it's ok
# def possibilities_ok_under_5(n):
#     if n == 0:
#         return 1
#     if n == 1 or n == 2:
#         return 2 ** n
#     else:
#         return 2 * (possibilities(n - 1)) - 1


#  This function works for all inputs, I believe. It counts all the valid combinations for a series of consecutive non-necessary adapters
@lru_cache
def possibilities(n):
    lst = [i for i in range(1, n + 1)]
    combs = []
    if n < 3:
        combs.append(())
    for r in range(1, n + 1):
        combs += [comb for comb in combinations(lst, r) if checkcomb(comb, n)]

    return len(combs)


#  Chech a combination is valid (respects the +3 jolt constraint)
def checkcomb(comb, n):
    if comb[0] > 3 or comb[-1] < n - 2:
        return False
    if len(comb) == 1:
        return True
    return all(v2 - v1 <= 3 for v1, v2 in zip(comb, comb[1:]))


def solve_day10(data):
    values = defaultdict(int)
    for delta in (val2 - val1 for val1, val2 in zip(data, data[1:])):
        values[delta] += 1

    part1 = values[1] * values[3]
    print("part1:", part1)

    groupszeros = (
        (len(list(l)))
        for v, l in groupby([int(is_necessary(data, idx)) for idx in range(len(data))])
        if v == 0
    )

    part2 = prod(possibilities(g) for g in groupszeros)
    print("part 2:", part2)

    return part1, part2


@timer
def main():
    with open("inputs/day10.txt") as f:
        data = sorted([int(ln.strip()) for ln in f])

    data.append(data[-1] + 3)
    data.append(0)
    data = sorted(data)

    print(solve_day10(data))


if __name__ == "__main__":
    main()
