from utils import timer


@timer
def solve_part1(data):
    pass


@timer
def solve_part2(data):
    pass


def solve_day6(data):
    part1 = solve_part1(data)
    part2 = solve_part2(data)

    return part1, part2


@timer
def main():
    yes = []
    current = set()
    with open("inputs/day6.txt") as f:
        for line in f:
            if line == '\n':
                yes.append(current)
                current = set()
            else:
                for c in line.strip():
                    current.add(c)

    yes.append(current)
    print(sum(len(group) for group in yes))


    # print(solve_day6(data))


if __name__ == "__main__":
    main()
