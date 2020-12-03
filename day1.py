from itertools import combinations
from math import prod


def solve_day1(data, comb_len, target_sum):
    return next(
        prod(comb)
        for comb in combinations(data, comb_len)
        if sum(comb) == target_sum
    )


def main():
    """
    Solves day1 puzzle
    >>> in_data = [1721, 979, 366, 299, 675, 1456]
    >>> solve_day1(in_data, 2, 2020)
    514579
    >>> solve_day1(in_data, 3, 2020)
    241861950
    """
    with open("inputs/day1.txt") as f:
        data = [int(x) for x in f]
    print(solve_day1(data, 2, 2020))
    print(solve_day1(data, 3, 2020))


if __name__ == "__main__":
    main()
