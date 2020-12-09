from itertools import combinations

from utils import timer


def part2(data, part1):
    for i, val in enumerate(data):
        sz = 0
        acc = 0
        while acc < part1:
            acc += data[i + sz]
            if acc == part1:
                return data[i: i + sz + 1]
            sz += 1


def solve_day9(data):
    part1 = None
    for i in range(25, len(data)):
        val = data[i]
        nums = data[i - 25:i]
        if not any(sum(comb) == val for comb in combinations(nums, 2)):
            part1 = val
            break

    result = sorted(part2(data, part1))
    return part1, result[0] + result[-1]


@timer
def main():
    with open("inputs/day9.txt") as f:
        data = [int(ln.strip()) for ln in f]

    print(solve_day9(data))


if __name__ == "__main__":
    main()
