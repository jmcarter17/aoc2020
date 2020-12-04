from utils import timer


def process_line(ln):
    return ln


def check_byr(byr):
    return 1920 <= int(byr) <= 2002


def check_iyr(iyr):
    return 2010 <= int(iyr) <= 2020


def check_eyr(eyr):
    return 2020 <= int(eyr) <= 2030


def check_hgt(hgt):
    return any(
        (
            hgt[2:] == "in" and 59 <= int(hgt[:2]) <= 76,
            hgt[3:] == "cm" and 150 <= int(hgt[:3]) <= 193,
        )
    )


def check_hcl(hcl):
    return all(
        (hcl[0] == "#", len(hcl) == 7, all(c in "0123456789abcdef" for c in hcl[1:]))
    )


def check_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_pid(pid):
    return len(pid) == 9 and int(pid) > -1


@timer
def solve_part1(data):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valids = [pp for pp in data if all(req in pp for req in required)]

    return valids


@timer
def solve_part2(data):
    return sum(
        all(
            (
                check_byr(pp["byr"]),
                check_ecl(pp["ecl"]),
                check_eyr(pp["eyr"]),
                check_hcl(pp["hcl"]),
                check_hgt(pp["hgt"]),
                check_iyr(pp["iyr"]),
                check_pid(pp["pid"]),
            )
        )
        for pp in data
    )


def solve_day4(data):
    part1 = solve_part1(data)
    part2 = solve_part2(part1)

    return len(part1), part2


def main():
    with open("inputs/day4.txt") as f:
        data = [{}]
        for line in f:
            items = line.split()
            if len(items) == 0:
                data.append({})
            else:
                for item in items:
                    k, v = item.split(":")
                    data[-1].update({k: v})

    print(solve_day4(data))


if __name__ == "__main__":
    main()
