from utils import timer


def solve_day6(data):
    part1 = []
    part2 = []
    group = []
    for ln in data:
        if ln == set():
            part1.append(set.union(*group))
            part2.append(set.intersection(*group))
            group.clear()
        else:
            group.append(ln)

    part1.append(set.union(*group))
    part2.append(set.intersection(*group))

    result1 = sum(len(group) for group in part1)
    result2 = sum(len(group) for group in part2)

    return result1, result2


@timer
def main():
    with open("inputs/day6.txt") as f:
        data = [set(ln.strip()) for ln in f]

    print(solve_day6(data))


if __name__ == "__main__":
    main()
