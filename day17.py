from itertools import count
import numpy as np

from utils import timer


@timer
def main():
    with open("inputs/day17.txt") as f:
        data = np.array([np.array(process_line(ln.strip())) for ln in f])

    print(solve_day17(data))
    # data = np.expand_dims(data, axis=0)
    # data = np.expand_dims(data, axis=0)
    # data = pad_data(data)
    # it = np.nditer(data, flags=['multi_index'])
    # # while not it.finished:
    # #     print(it.value, it.multi_index)
    # #     it.iternext()
    #
    # # print(list(np.ndindex(data.shape)))
    # print(len(get_neighbors(data, (1, 1, 1))))


def process_line(ln):
    return [1 if i == "#" else 0 for i in ln]


def get_neighbors(data, idx):
    neighbors = []
    for index in np.ndindex(data.shape):
        if all(abs(np.array(idx) - np.array(index)) <= 1) and index != idx:
            neighbors.append(index)

    return neighbors


@timer
def solve_day17(data):
    result1 = part1(data)
    result2 = part2(data)

    return result1, result2


@timer
def part1(data):
    data = np.expand_dims(data, axis=0)

    for _ in range(6):
        data = conway3d(data)

    return sum(data.flatten())


@timer
def part2(data):
    data = np.expand_dims(data, axis=0)
    data = np.expand_dims(data, axis=0)

    for _ in range(6):
        data = conway4d(data)

    return sum(data.flatten())


def pad_data(data):
    return np.pad(data, 1, mode="constant")


def count_on_neighbors(data, idx):
    # neighbors = get_neighbors(data, idx)
    i, j, k = idx
    xrange = range(max(0, i - 1), min(data.shape[0], i + 2))
    yrange = range(max(0, j - 1), min(data.shape[1], j + 2))
    zrange = range(max(0, k - 1), min(data.shape[2], k + 2))

    neighbors = [
        (x, y, z)
        for x in xrange
        for y in yrange
        for z in zrange
        if (x, y, z) != (i, j, k)
    ]

    return sum(data[neighbor] for neighbor in neighbors)


def count_on_neighbors_4d(data, i, j, k, l):
    xrange = range(max(0, i - 1), min(data.shape[0], i + 2))
    yrange = range(max(0, j - 1), min(data.shape[1], j + 2))
    zrange = range(max(0, k - 1), min(data.shape[2], k + 2))
    wrange = range(max(0, l - 1), min(data.shape[3], l + 2))

    neighbors = [
        (x, y, z, w)
        for x in xrange
        for y in yrange
        for z in zrange
        for w in wrange
        if (x, y, z, w) != (i, j, k, l)
    ]

    return sum(data[neighbor] for neighbor in neighbors)


def conway3d(data):
    data = pad_data(data)
    copy = np.copy(data)
    for i, layer in enumerate(data):
        for j, row in enumerate(layer):
            for k, col in enumerate(row):
                num_on = count_on_neighbors(copy, (i, j, k))
                if data[i, j, k] == 1:
                    if not 2 <= num_on <= 3:
                        data[i, j, k] = 0
                else:
                    if num_on == 3:
                        data[i, j, k] = 1

    return data


def conway4d(data):
    data = pad_data(data)
    copy = np.copy(data)
    for i, hyper in enumerate(data):
        for j, layer in enumerate(hyper):
            for k, row in enumerate(layer):
                for l, col in enumerate(row):
                    num_on = count_on_neighbors_4d(copy, i, j, k, l)
                    if data[i, j, k, l] == 1:
                        if not 2 <= num_on <= 3:
                            data[i, j, k, l] = 0
                    else:
                        if num_on == 3:
                            data[i, j, k, l] = 1

    return data


if __name__ == "__main__":
    main()
