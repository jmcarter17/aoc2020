def process_line(ln):
    policy, letter, pwd = ln.split()
    policy = get_policy_range(policy)
    letter = letter[0]
    return policy, letter, pwd


def check_pwd_policy1(processed):
    """
    Solve day2 puzzle policy1

    >>> check_pwd_policy1(process_line("1-3 a: abcde"))
    True
    >>> check_pwd_policy1(process_line("1-3 b: cdefg"))
    False
    >>> check_pwd_policy1(process_line("2-9 c: ccccccccc"))
    True
    """
    policy, letter, pwd = processed
    return pwd.count(letter) in policy


def check_pwd_policy2(processed):
    """
    Solve day2 puzzle policy2

    >>> check_pwd_policy2(process_line("1-3 a: abcde"))
    True
    >>> check_pwd_policy2(process_line("1-3 b: cdefg"))
    False
    >>> check_pwd_policy2(process_line("2-9 c: ccccccccc"))
    False
    """
    policy, letter, pwd = processed
    idx1 = policy[0] - 1
    idx2 = policy[-1] - 1
    return (pwd[idx1] == letter) ^ (pwd[idx2] == letter)


def get_policy_range(data):
    vals = [int(val) for val in data.split("-")]
    return range(vals[0], vals[1] + 1)


def solve_day2(data):
    part1 = sum(check_pwd_policy1(ln) for ln in data)
    part2 = sum(check_pwd_policy2(ln) for ln in data)
    return part1, part2


def main():
    with open("inputs/day2.txt") as f:
        lines = [process_line(line) for line in f]

    print(solve_day2(lines))


if __name__ == "__main__":
    main()
