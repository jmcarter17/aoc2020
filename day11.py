from functools import lru_cache
from itertools import combinations

import numpy as np
from utils import timer


@lru_cache
def grid_directions():
    return set(combinations((-1, 1, 0, 1, -1), 2))


def all_neighbors(idx, shape):
    return (
        next_idx(idx, d)
        for d in grid_directions()
        if valid_idx(next_idx(idx, d), shape)
    )


def next_idx(idx, direction):
    return tuple(sum(x) for x in zip(idx, direction))


def valid_idx(idx, shape):
    return all(0 <= idx[i] < shape[i] for i in (0, 1))


def count_on_neighbors(data, idx):
    return sum(data[neighbor] == "#" for neighbor in all_neighbors(idx, data.shape))


def count_first_view(data, idx):
    return sum(check_dir(data, idx, d) for d in set(combinations((-1, 1, 0, 1, -1), 2)))


def check_dir(data, idx, direction):
    idx = next_idx(idx, direction)

    while valid_idx(idx, data.shape) and data[idx] == ".":
        idx = next_idx(idx, direction)
    if not valid_idx(idx, data.shape):
        return False
    return data[idx] == "#"


def automaton(data, count_fn, lmt):
    copy = np.copy(data)
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i, j] == ".":
                continue
            num_on = count_fn(copy, (i, j))
            if data[i, j] == "L" and num_on == 0:
                data[i, j] = "#"
            elif data[i, j] == "#" and num_on >= lmt:
                data[i, j] = "L"


def count_occupied(data):
    return sum(
        data[i, j] == "#" for i in range(data.shape[0]) for j in range(data.shape[1])
    )


@timer
def part1(data):
    prev = None
    while not (data == prev).all():
        prev = np.copy(data)
        automaton(data, count_on_neighbors, 4)

    return count_occupied(data)


@timer
def part2(data):
    prev = None
    while not (data == prev).all():
        prev = np.copy(data)
        automaton(data, count_first_view, 5)

    return count_occupied(data)


@timer
def solve_day11(data):
    copy = np.copy(data)
    result1 = part1(copy)
    result2 = part2(data)

    return result1, result2


@timer
def main():
    with open("inputs/day11.txt") as f:
        data = np.array([list(ln.strip()) for ln in f])

    print(solve_day11(data))


if __name__ == "__main__":
    main()
