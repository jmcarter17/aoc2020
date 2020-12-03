from itertools import combinations
from math import prod
from utils import timer


@timer
def solve_day1(data, comb_len, target_sum):
    """
    Solves day1 puzzle
    >>> in_data = [1721, 979, 366, 299, 675, 1456]
    >>> solve_day1(in_data, 2, 2020)
    514579
    >>> solve_day1(in_data, 3, 2020)
    241861950
    """
    return next(
        prod(comb)
        for comb in combinations(data, comb_len)
        if sum(comb) == target_sum
    )


# @timer
# def solve_part1(data):
#     for i, val1 in enumerate(data):
#         for val2 in data[i:]:
#             if val1 + val2 == 2020:
#                 return val1*val2
#
#
# @timer
# def solve_part2(data):
#     for i, val1 in enumerate(data):
#         for j, val2 in enumerate(data[i:]):
#             for val3 in data[j:]:
#                 if val1 + val2 + val3 == 2020:
#                     return val1*val2*val3


def main():
    with open("inputs/day1.txt") as f:
        data = [int(x) for x in f]
    print(solve_day1(data, 2, 2020))
    print(solve_day1(data, 3, 2020))

    # print(solve_part1(data))
    # print(solve_part2(data))


if __name__ == "__main__":
    main()
