from collections import deque

from utils import timer


@timer
def main():
    data_input = "476138259"
    data = [int(c) for c in data_input]

    print(solve_day23(data))


@timer
def solve_day23(data):
    result1 = part1(data)
    result2 = part2(data)

    return result1, result2


@timer
def part1(data):
    links = run_cups_game(data, len(data), 100)

    nxt = links[1]
    result = ""
    while nxt != 1:
        result += str(nxt)
        nxt = links[nxt]

    return result


@timer
def part2(data):
    links = run_cups_game(data, 1000000, 10000000)
    return links[1] * links[links[1]]


def run_cups_game(data, size, num_iteration):
    gamedata = data + list(range(len(data) + 1, size + 1))
    links = {
        val: gamedata[(idx + 1) % len(gamedata)] for idx, val in enumerate(gamedata)
    }
    current = gamedata[0]
    for _ in range(num_iteration):
        current = move_cups(links, current, size)

    return links


def move_cups(links, current, size):
    cup1 = links[current]
    cup2 = links[cup1]
    cup3 = links[cup2]
    selection = (cup1, cup2, cup3)

    dest = current - 1
    while dest in selection or dest < 1:
        if dest in selection:
            dest -= 1
        if dest < 1:
            dest = size

    links[current], links[cup3], links[dest] = links[cup3], links[dest], cup1
    return links[current]


# def cups_move(data):
#     selects = data[1:4]
#     data = data[0:1] + data[4:]
#     destlabel = data[0] - 1
#     while destlabel in selects:
#         destlabel -= 1
#
#     if destlabel == 0:
#         destlabel = max(data)
#
#     destidx = data.index(destlabel)
#     data = data[:destidx+1] + selects[:] + data[destidx+1:]
#     data.append(data.pop(0))
#     return data


if __name__ == "__main__":
    main()
