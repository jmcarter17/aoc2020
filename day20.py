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
            if ln == "\n":
                pass
            elif "Tile" in ln:
                idx = int(ln.strip()[5:-1])
                tiles[idx] = []
            else:
                numbers = [int(c == "#") for c in ln.strip()]
                tiles[idx].append(numbers)

    tiles = {k: np.array(val) for k, val in tiles.items()}

    print(solve_day20(tiles))


@timer
def solve_day20(tiles):
    tiles_matches = match_tiles(tiles)
    corners = get_corners(tiles_matches)
    result1 = part1(corners)
    result2 = part2(tiles, tiles_matches, corners)

    return result1, result2


@timer
def part1(corners):
    return prod(corners)


def match_tiles(tiles):
    tiles_matches = defaultdict(dict)
    for t1, t2 in combinations(tiles, 2):
        for t1_side in "udlr":
            side_t1 = get_side(tiles[t1], t1_side)
            for t2_side in "udlr":
                side_t2 = get_side(tiles[t2], t2_side)
                if np.all(side_t1 == side_t2) or np.all(side_t1 == np.flip(side_t2)):
                    tiles_matches[t1][t1_side] = t2
                    tiles_matches[t2][t2_side] = t1
                    break

    return tiles_matches


def get_corners(tiles_matches):
    return [t for t in tiles_matches if len(tiles_matches[t]) == 2]


@timer
def part2(tiles, tiles_matches, corners):
    dims = int(len(tiles) ** 0.5)
    topleft_id = corners[0]
    if "l" in tiles_matches[topleft_id]:
        tiles[topleft_id] = np.fliplr(tiles[topleft_id])
    if "u" in tiles_matches[topleft_id]:
        tiles[topleft_id] = np.flipud(tiles[topleft_id])

    image_id = []
    image = []
    for row_idx in range(dims):
        image.append([])
        image_id.append([])
        if row_idx == 0:
            image_id[0].append(topleft_id)
            image[0].append(tiles[topleft_id][1:-1, 1:-1])
        else:
            uptile = tiles[image_id[row_idx - 1][0]]
            maybes = tiles_matches[image_id[row_idx - 1][0]].values()
            tile_id = find_match_down(tiles, uptile, maybes)
            tile = tiles[tile_id][1:-1, 1:-1]
            image[row_idx].append(tile)
            image_id[row_idx].append(tile_id)
        for col_idx in range(1, dims):
            lefttile = tiles[image_id[row_idx][col_idx - 1]]
            maybes = tiles_matches[image_id[row_idx][col_idx - 1]].values()
            tile_id = find_match_right(tiles, lefttile, maybes)
            tile = tiles[tile_id][1:-1, 1:-1]
            image[row_idx].append(tile)
            image_id[row_idx].append(tile_id)

    image = np.array(image)
    image_unrolled = []
    for i in range(dims):
        for row in range(8):
            for j in range(dims):
                image_unrolled.extend(image[i, j, row])

    image_2d = np.reshape(image_unrolled, (dims*8, dims*8))

    count = 0
    monster = sea_monster()
    tries = 0
    while not count:
        tries += 1
        for i in range(image_2d.shape[0] - 3):
            for j in range(image_2d.shape[1] - 20):
                window = image_2d[i : i + 3, j : j + 20]
                is_monster = np.logical_and(window, monster)
                if np.all(is_monster == monster):
                    count += 1

        if tries == 4:
            image_2d = np.flipud(image_2d)
        else:
            image_2d = np.rot90(image_2d)

        if tries == 8:
            break

    return sum(sum(image_2d)) - count * sum(sum(monster))


def find_match_down(tiles, fixed_tile, options):
    to_match = get_side(fixed_tile, "d")
    found = False
    flip = False
    for t in options:
        if t in tiles:
            for i, side in enumerate(get_all_sides(tiles[t])):
                if np.all(side == to_match):
                    found = True
                    break
                elif np.all(np.flip(side) == to_match):
                    found = True
                    flip = True
                    break
            if found:
                break

    tile_id = t
    for _ in range(i):
        tiles[tile_id] = np.rot90(tiles[tile_id])
    if i > 1:
        tiles[tile_id] = np.fliplr(tiles[tile_id])
    if flip:
        tiles[tile_id] = np.fliplr(tiles[tile_id])

    return tile_id


def find_match_right(tiles, fixed_tile, options):
    to_match = get_side(fixed_tile, "r")
    found = False
    flip = False
    for t in options:
        if t in tiles:
            for i, side in enumerate(get_all_sides(tiles[t])):
                if np.all(side == to_match):
                    found = True
                    break
                elif np.all(np.flip(side) == to_match):
                    found = True
                    flip = True
                    break
            if found:
                break

    tile_id = t
    for _ in range((i - 3) % 4):
        tiles[tile_id] = np.rot90(tiles[tile_id])
    if i <= 1:
        tiles[tile_id] = np.flipud(tiles[tile_id])
    if flip:
        tiles[tile_id] = np.flipud(tiles[tile_id])

    return tile_id


def get_side(tile, side):
    if side == "u":
        return tile[0]
    elif side == "d":
        return tile[-1]
    elif side == "l":
        return tile[:, 0]
    elif side == "r":
        return tile[:, -1]


def get_all_sides(tile):
    return [get_side(tile, side) for side in "urdl"]


def sea_monster():
    monster = ("                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   ")
    return np.array([[1 if c == "#" else 0 for c in line] for line in monster])


if __name__ == "__main__":
    main()
