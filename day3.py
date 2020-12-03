from math import prod


def get_index(ln, lw, step_right):
    return (step_right * ln) % lw


def check_line(line, ln, lw, step_right):
    return line[get_index(ln, lw, step_right)] == '#'


def solve_day3(data):
    lw = len(data[0])
    part1 = sum(check_line(line, ln, lw, 3) for ln, line in enumerate(data))
    part2 = [
        sum(check_line(line, ln, lw, 1) for ln, line in enumerate(data)),
        part1,
        sum(check_line(line, ln, lw, 5) for ln, line in enumerate(data)),
        sum(check_line(line, ln, lw, 7) for ln, line in enumerate(data)),
        sum(check_line(line, ln//2, lw, 1) for ln, line in enumerate(data) if ln % 2 == 0)
    ]
    print(part2)

    return part1, prod(part2)


def main():
    with open("inputs/day3.txt") as f:
        data = [line.strip() for line in f]

    print(solve_day3(data))


if __name__ == "__main__":
    main()
