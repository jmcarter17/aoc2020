from utils import timer


def process_line(ln):
    return ln


@timer
def solve_part1(data):
    required = ["byr", 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valids = []
    for pp in data:
        valid = True
        for req in required:
            if req not in pp:
                valid = False
                break
        if valid:
            valids.append(pp)

    return valids


def check_byr(pp):
    try:
        return 1920 <= int(pp['byr']) <= 2002
    except Exception:
        return False


def check_iyr(pp):
    try:
        return 2010 <= int(pp['iyr']) <= 2020
    except Exception:
        return False


def check_eyr(pp):
    try:
        return 2020 <= int(pp['eyr']) <= 2030
    except Exception:
        return False


def check_hgt(pp):
    try:
        if len(pp['hgt']) == 4:
            return pp['hgt'][2:] == 'in' and 59 <= int(pp['hgt'][:2]) <= 76
        elif len(pp['hgt']) == 5:
            return pp['hgt'][3:] == 'cm' and 150 <= int(pp['hgt'][:3]) <= 193
        else:
            return False
    except Exception:
        return False


def check_hcl(pp):
    try:
        if len(pp['hcl']) != 7 or pp['hcl'][0] != '#':
            return False
        else:
            for c in pp['hcl'][1:]:
                if c not in '0123456789abcdef':
                    return False
            return True
    except Exception:
        return False


def check_ecl(pp):
    try:
        if pp['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        return True
    except Exception:
        return False


def check_pid(pp):
    try:
        if len(pp['pid']) != 9:
            return False
        id = int(pp['pid'])
        return id != -1
    except Exception:
        return False



@timer
def solve_part2(data, validpp):
    valids = 0
    for pp in validpp:
        if all((check_byr(pp), check_ecl(pp), check_eyr(pp), check_hcl(pp), check_hgt(pp), check_iyr(pp), check_pid(pp))):
            valids += 1
    return valids


def solve_day4(data):
    part1 = solve_part1(data)
    part2 = solve_part2(data, part1)

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
