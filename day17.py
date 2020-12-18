from itertools import count
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
    copy = np.copy(data)
    it = np.nditer(data, flags=['multi_index'])
    while not it.finished:
        idx = it.multi_index
        num_on = count_on_neighbors(copy, idx)
        if data[idx] == 1:
            if not 2 <= num_on <= 3:
                data[idx] = 0
        else:
            if num_on == 3:
                data[idx] = 1
        it.iternext()

    return data


def pad_data(data):
    return np.pad(data, 1, mode="constant")


def count_on_neighbors(data, idx):
    return sum(data[neighbor] for neighbor in get_neighbors(data, idx))


def get_neighbors(data, idx):
    if len(data.shape) == 3:
        return get_neighbors_3d(data, idx)
    elif len(data.shape) == 4:
        return get_neighbors_4d(data, idx)


def get_neighbors_3d(data, idx):
    i, j, k = idx
    xrange = range(max(0, i - 1), min(data.shape[0], i + 2))
    yrange = range(max(0, j - 1), min(data.shape[1], j + 2))
    zrange = range(max(0, k - 1), min(data.shape[2], k + 2))

    return (
        (x, y, z)
        for x in xrange
        for y in yrange
        for z in zrange
        if (x, y, z) != (i, j, k)
    )


def get_neighbors_4d(data, idx):
    i, j, k, l = idx
    xrange = range(max(0, i - 1), min(data.shape[0], i + 2))
    yrange = range(max(0, j - 1), min(data.shape[1], j + 2))
    zrange = range(max(0, k - 1), min(data.shape[2], k + 2))
    wrange = range(max(0, l - 1), min(data.shape[3], l + 2))

    return (
        (x, y, z, w)
        for x in xrange
        for y in yrange
        for z in zrange
        for w in wrange
        if (x, y, z, w) != (i, j, k, l)
    )


if __name__ == "__main__":
    main()
