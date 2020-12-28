from utils import timer


@timer
def main():
    with open("inputs/day22.txt") as f:
        lines = [ln.strip() for ln in f]

    idx_emptyln = lines.index("")
    data = {
        "p1": [int(val) for val in lines[1:idx_emptyln]],
        "p2": [int(val) for val in lines[idx_emptyln + 2 :]],
    }

    print(solve_day22(data))


@timer
def solve_day22(data):
    result1 = part1(data)
    result2 = part2(data)

    return result1, result2


@timer
def part1(data):
    return scoredeck(max(combat(data["p1"][:], data["p2"][:])))


@timer
def part2(data):
    _, p1, p2 = recursive_combat(data["p1"][:], data["p2"][:])
    return scoredeck(max(p1, p2))


def combat(p1, p2):
    while len(p1) and len(p2):
        v1, v2 = p1.pop(0), p2.pop(0)
        if v1 > v2:
            p1.extend((v1, v2))
        else:
            p2.extend((v2, v1))

    return p1, p2


def scoredeck(deck):
    return sum((i+1) * v for i, v in enumerate(reversed(deck)))


def recursive_combat(p1, p2):
    seen = {"p1": set(), "p2": set()}
    while len(p1) and len(p2):
        if tuple(p1) in seen["p1"] or tuple(p2) in seen["p2"]:
            return "p1", p1, p2
        seen["p1"].add(tuple(p1))
        seen["p2"].add(tuple(p2))

        v1, v2 = p1.pop(0), p2.pop(0)
        if check_winner(v1, v2, p1, p2) == "p1":
            p1.extend((v1, v2))
        else:
            p2.extend((v2, v1))

    winner = "p1" if p1 else "p2"

    return winner, p1, p2


def check_winner(v1, v2, p1, p2):
    if len(p1) >= v1 and len(p2) >= v2:
        return recursive_combat(p1[:v1], p2[:v2])[0]

    return "p1" if v1 > v2 else "p2"


if __name__ == "__main__":
    main()
