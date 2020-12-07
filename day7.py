from utils import timer


_BAG = 'shiny gold'


def get_rules(data):
    rules = [process_line(ln) for ln in data]
    return dict(rules)


def process_line(ln):
    ln = ln.replace(" bags", "").replace("bag", "").replace(".", "")
    items = ln.split(" contain ")
    items[1] = items[1].split(", ")
    item = {}
    for c in items[1]:
        num = c[0:1]
        key = c[2:].strip()
        if num != 'n':
            item[key] = int(num)
    items[1] = item
    return items


def check_recur(rules, canhold, k):
    if k in canhold:
        return True
    elif _BAG in rules[k]:
        canhold.add(k)
        return True
    else:
        for v in rules[k]:
            if check_recur(rules, canhold, v):
                canhold.add(k)
                return True
        return False


def count_contains(rules, k):
    if rules[k] == {}:
        return 0
    else:
        acc = sum(rules[k].values())
        return sum(count_contains(rules, v) * rules[k][v] for v in rules[k]) + acc


def solve_day7(data):
    rules = get_rules(data)

    canhold = set()
    for k, v in rules.items():
        check_recur(rules, canhold, k)

    contains = count_contains(rules, _BAG)

    return len(canhold), contains


@timer
def main():
    with open("inputs/day7.txt") as f:
        data = [ln.strip() for ln in f]

    print(solve_day7(data))


if __name__ == "__main__":
    main()
