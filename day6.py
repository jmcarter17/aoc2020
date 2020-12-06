from utils import timer


def solve_day6(data):
    part1 = []
    part2 = []
    set1 = set()
    set2 = set(list('abcdefghijklmnopqrstuvwxyz'))
    for ln in data:
        if ln == '':
            part1.append(set1)
            part2.append(set2)
            set1 = set()
            set2 = set(list('abcdefghijklmnopqrstuvwxyz'))
        else:
            setln = set(list(ln))
            set1 = set1.union(setln)
            set2 = set2.intersection(setln)

    part1.append(set1)
    part2.append(set2)

    result1 = sum(len(group) for group in part1)
    result2 = sum(len(group) for group in part2)

    return result1, result2


@timer
def main():
    with open("inputs/day6.txt") as f:
        data = [ln.strip() for ln in f]

    print(solve_day6(data))


if __name__ == "__main__":
    main()
