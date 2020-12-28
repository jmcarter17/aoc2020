from itertools import product

from utils import timer


@timer
def main():
    with open("inputs/day19.txt") as f:
        data = [ln.strip() for ln in f]
        idx_split = data.index("")
        rules = dict((tuple(rule.split(": ")) for rule in data[:idx_split]))
        messages = data[idx_split + 1 :]
        for k, v in rules.items():
            if v == '"a"' or v == '"b"':
                rules[k] = [v[1]]
            else:
                vs = v.split(" | ")
                rules[k] = [x.split() for x in vs]

    print(solve_day19(rules, messages))


@timer
def solve_day19(rules, messages):
    result1 = part1(rules, messages)
    # result2 = part2(rules, messages)

    return result1, None


@timer
def part1(rules, messages):
    matches_zero = set(eval_rules("0", rules))
    return sum((m in matches_zero) for m in messages)


@timer
def part2(rules, messages):
    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]
    matches_zero = eval_rules('0', rules)

    return sum((m in matches_zero) for m in messages)


def eval_rules(idx, rules):
    if all(isinstance(x, str) for x in rules[idx]):
        return rules[idx]
    else:
        rules[idx] = [
            "".join(char)
            for subrule in ((eval_rules(x, rules) for x in rule) for rule in rules[idx])
            for char in product(*subrule)
        ]

        return rules[idx]


if __name__ == "__main__":
    main()
