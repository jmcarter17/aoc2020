from itertools import product
import numpy as np
from utils import timer


@timer
def main():
    with open("inputs/day17.txt") as f:
        data = np.array([np.array(process_line(ln.strip())) for ln in f])

    print(solve_day17(data))


def process_line(ln):
    return [1 if i == "#" else 0 for i in ln]


@timer
def solve_day17(data):
    result1 = part1(data)
    result2 = part2(data)

    return result1, result2


@timer
def part1(data):
    data = np.expand_dims(data, axis=0)

    for _ in range(6):
        data = hyper_conway(data)

    return sum(data.flatten())


@timer
def part2(data):
    data = np.expand_dims(data, axis=0)
    data = np.expand_dims(data, axis=0)

    for _ in range(6):
        data = hyper_conway(data)

    return sum(data.flatten())


def hyper_conway(data):
    data = pad_data(data)
    next_gen = np.zeros_like(data)
    for idx in np.ndindex(data.shape):
        sum_neighbors = count_on_neighbors(data, idx)
        next_gen[idx] = any(
            (
                sum_neighbors == 3,
                data[idx] == 1 and 2 == sum_neighbors
            )
        )

    return next_gen


def pad_data(data):
    return np.pad(data, 1, mode="constant")


def count_on_neighbors(data, idx):
    return sum(data[neighbor] for neighbor in get_neighbors(data, idx))


def get_neighbors(data, idx):
    ranges = (
        range(max(0, d - 1), min(data.shape[i], d + 2)) for i, d in enumerate(idx)
    )
    return filter(
        lambda x: x != idx,
        product(*ranges),
    )


if __name__ == "__main__":
    main()
