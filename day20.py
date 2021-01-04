from collections import defaultdict
from itertools import combinations
from math import prod
import numpy as np

from utils import timer


@timer
def main():
    tiles = {}
    with open("inputs/day20.txt") as f:
        idx = -1
        for ln in f:
            if "Tile" in ln:
                idx = int(ln.strip()[5:-1])
                tiles[idx] = []
            elif ln == "\n":
                pass
            else:
                tiles[idx].append(ln.strip())

    print(solve_day20(tiles))


@timer
def solve_day20(tiles):
    # print(tiles)
    result1 = part1(tiles)
    result2 = part2(tiles)

    return result1, result2


@timer
def part1(tiles):
    tiles_matches = defaultdict(int)
    for t1, t2 in combinations(tiles, 2):
        for t1_side in 'udlr':
            for t2_side in 'udlr':
                side_t1, side_t2 = get_side(tiles[t1], t1_side), get_side(tiles[t2], t2_side)

                if side_t1 == side_t2 or side_t1 == side_t2[::-1]:
                    tiles_matches[t1] += 1
                    tiles_matches[t2] += 1

    corners = [t for t in tiles_matches if tiles_matches[t] == 2]

    return prod(corners)



@timer
def part2(tiles):
    pass


def get_side(tile, side):
    if side == "u":
        return tile[0]
    elif side == "d":
        return tile[-1]
    elif side == "l":
        return "".join(row[0] for row in tile)
    elif side == "r":
        return "".join(row[-1] for row in tile)


if __name__ == "__main__":
    main()
