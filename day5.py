from utils import timer


def midpoint(lo, hi):
    return (hi + lo) // 2


def find_section_id(code, lo_char, high_val):
    lo, hi = 0, high_val
    for c in code:
        mid = midpoint(lo, hi)
        if c == lo_char:
            hi = mid
        else:
            lo = mid
    return lo


def get_row(ln):
    return find_section_id(ln[:7], 'F', 128)


def get_col(ln):
    return find_section_id(ln[7:], 'L', 8)


def get_id(ln):
    return get_row(ln) * 8 + get_col(ln)


@timer
def solve_part1(data):
    return data[-1]


@timer
def solve_part2(data):
    return next((a, b) for a, b in zip(data, data[1:]) if b - a != 1)[0] + 1


def solve_day5(data):
    part1 = solve_part1(data)
    part2 = solve_part2(data)

    return part1, part2


@timer
def main():
    with open("inputs/day5.txt") as f:
        data = sorted([get_id(ln.strip()) for ln in f])

    print(solve_day5(data))


if __name__ == "__main__":
    main()
