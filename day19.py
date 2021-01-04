import re

from utils import timer


@timer
def main():
    with open("inputs/day19.txt") as f:
        data = [ln.strip() for ln in f]

    idx_split = data.index("")
    rules = create_rules_dict(data[:idx_split])
    messages = data[idx_split + 1 :]

    print(solve_day19(rules, messages))


def create_rules_dict(data):
    rules = {}

    for ln in data:
        rule_id, options = ln.split(": ")
        rule_id = int(rule_id)

        rules[rule_id] = (
            options[1]
            if '"' in options
            else [tuple(map(int, option.split())) for option in options.split("|")]
        )

    return rules


@timer
def solve_day19(rules, messages):
    result1 = part1(rules, messages)
    result2 = part2(rules, messages)

    return result1, result2


@timer
def part1(rules, messages):
    rexp = re.compile(f"^{build_regexp(rules)}$")
    return sum(map(bool, map(rexp.match, messages)))


@timer
def part2(rules, messages):
    rules[8] = [(42,), (42, 8)]
    rules[11] = [(42, 31), (42, 11, 31)]
    return sum(len(message) in match(rules, message) for message in messages)


def build_regexp(rules, idx=0):
    rule = rules[idx]
    if type(rule) is str:
        return rule

    options = ["".join(build_regexp(rules, r) for r in option) for option in rule]
    return "(" + "|".join(options) + ")"


def match(rules, string, rule_idx=0, index=0):
    if index == len(string):
        return []

    rule = rules[rule_idx]
    if type(rule) is str:
        return [index + 1] if string[index] == rule else []

    matches = []
    for option in rule:
        sub_matches = [index]

        for sub_rule_idx in option:
            new_matches = []
            for idx in sub_matches:
                new_matches += match(rules, string, sub_rule_idx, idx)
            sub_matches = new_matches

        matches += sub_matches

    return matches


if __name__ == "__main__":
    main()
