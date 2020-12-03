def solve_day1_1(data):
    """
    Solves day1-1 puzzle

    >>> solve_day1_1([1721, 979, 366, 299, 675, 1456])
    514579
    """
    for i, val1 in enumerate(data):
        for val2 in data[i+1:]:
            if val1 + val2 == 2020:
                return val1 * val2


def solve_day1_2(data):
    """
    Solves day1-2 puzzle

    >>> solve_day1_2([1721, 979, 366, 299, 675, 1456])
    241861950
    """
    for i, val1 in enumerate(data):
        for j, val2 in enumerate(data[i+1:]):
            for val3 in data[j+1:]:
                if val1 + val2 + val3 == 2020:
                    return val1 * val2 * val3


def main():
    with open("inputs/day1.txt") as f:
        data = [int(x) for x in f]
    print(solve_day1_1(data))
    print(solve_day1_2(data))


if __name__ == "__main__":
    main()
