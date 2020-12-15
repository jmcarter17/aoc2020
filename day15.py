from utils import timer


@timer
def main():
    with open("inputs/day15.txt") as f:
        data = [int(x) for x in f.read().strip().split(",")]

    print(solve_day15(data))


@timer
def solve_day15(data):
    result1 = part1(data)
    result2 = part2(data)

    return result1, result2


@timer
def part1(data):
    return memory_game(data, 2020)


@timer
def part2(data):
    return memory_game(data, 30000000)


def memory_game(data, length):
    last_seen = {num: idx+1 for idx, num in enumerate(data)}
    current = 0
    for i in range(len(data)+1, length):
        nxt = 0 if current not in last_seen else i - last_seen[current]
        last_seen[current] = i
        current = nxt

    return current


def memory_game_brute(data, length):
    while len(data) < length:
        prev = data[-1]
        if data.count(prev) < 2:
            data.append(0)
        else:
            lastidx = data[::-1][1:].index(prev)
            data.append(lastidx + 1)

    return data[-1]


def test_cases():
    with open("inputs/day15test.txt") as f:
        data = [[int(x) for x in ln.strip().split(",")] for ln in f]
        for d in data:
            print(memory_game(d, 2020))


if __name__ == "__main__":
    main()
    test_cases()
