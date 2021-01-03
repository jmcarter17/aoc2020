from utils import timer


@timer
def main():
    with open("inputs/day24.txt") as f:
        data = [direction_to_grid(ln.strip()) for ln in f]

    print(solve_day24(data))


@timer
def solve_day24(data):
    blacks = part1(data)
    result1 = len(blacks)
    result2 = part2(blacks)

    return result1, result2


@timer
def part1(data):
    return set(x for x in data if data.count(x) % 2)


@timer
def part2(blacks):
    for _ in range(100):
        blacks = update_blacks(blacks)

    return len(blacks)


def update_blacks(blacks):
    to_black = set()
    to_white = set()
    checked = set()
    for tile in blacks:
        neighbors = get_neighbors(tile)
        white_neighbors = neighbors - blacks
        if len(white_neighbors) == 6 or len(white_neighbors) < 4:
            to_white.add(tile)
        for wtile in white_neighbors - checked:
            checked.add(wtile)
            if len(blacks & get_neighbors(wtile)) == 2:
                to_black.add(wtile)

    return (blacks - to_white) | to_black


def get_neighbors(tile):
    return {
        (tile[0] + 1, tile[1]),
        (tile[0] - 1, tile[1]),
        (tile[0], tile[1] + 1),
        (tile[0], tile[1] - 1),
        (tile[0] + 1, tile[1] - 1),
        (tile[0] - 1, tile[1] + 1),
    }


def reduce_direction(direction):
    commands = get_bearings(direction)
    lc = len(commands)
    while True:
        remove_opposites(commands)
        replace_adjacents(commands)
        if len(commands) == lc:
            break
        lc = len(commands)

    return "".join(sorted(commands))


def remove_opposites(commands):
    remove_opp(commands, "e", "w")
    remove_opp(commands, "se", "nw")
    remove_opp(commands, "ne", "sw")


def remove_opp(commands, dir1, dir2):
    nbdir1 = commands.count(dir1)
    nbdir2 = commands.count(dir2)
    for _ in range(min(nbdir1, nbdir2)):
        commands.remove(dir1)
        commands.remove(dir2)


def replace_adjacents(commands):
    replace_adj(commands, "nw", "e", "ne")
    replace_adj(commands, "ne", "w", "nw")
    replace_adj(commands, "sw", "e", "se")
    replace_adj(commands, "se", "w", "sw")
    replace_adj(commands, "se", "ne", "e")
    replace_adj(commands, "sw", "nw", "w")


def replace_adj(commands, dir1, dir2, repl):
    nbdir1 = commands.count(dir1)
    nbdir2 = commands.count(dir2)
    for _ in range(min(nbdir1, nbdir2)):
        commands.remove(dir1)
        commands.remove(dir2)
        commands.append(repl)


def get_bearings(direction):
    ptr = 0
    commands = []
    while ptr < len(direction):
        c1 = direction[ptr]
        if c1 in "ew":
            commands.append(c1)
            ptr += 1
        else:
            commands.append(direction[ptr : ptr + 2])
            ptr += 2

    return commands


def direction_to_grid(direction):
    pos = (0, 0)
    bearings = get_bearings(direction)
    for b in bearings:
        pos = step(pos, bearing_to_grid(b))

    return pos


def bearing_to_grid(bearing):
    if bearing == "e":
        return 1, 0
    elif bearing == "w":
        return -1, 0
    elif bearing == "ne":
        return 0, 1
    elif bearing == "sw":
        return 0, -1
    elif bearing == "nw":
        return -1, 1
    elif bearing == "se":
        return 1, -1


def step(init, grid_dir):
    return init[0] + grid_dir[0], init[1] + grid_dir[1]


def test_reduce_direction():
    assert reduce_direction("e") == "e"
    assert reduce_direction("w") == "w"
    assert reduce_direction("se") == "se"
    assert reduce_direction("ne") == "ne"
    assert reduce_direction("sw") == "sw"
    assert reduce_direction("nw") == "nw"

    assert reduce_direction("ew") == ""
    assert reduce_direction("eew") == "e"
    assert reduce_direction("eww") == "w"

    assert reduce_direction("swne") == ""
    assert reduce_direction("swnene") == "ne"
    assert reduce_direction("swswne") == "sw"

    assert reduce_direction("nwse") == ""
    assert reduce_direction("nwsese") == "se"
    assert reduce_direction("nwnwse") == "nw"

    assert reduce_direction("nwe") == "ne"
    assert reduce_direction("new") == "nw"
    assert reduce_direction("sew") == "sw"
    assert reduce_direction("swe") == "se"
    assert reduce_direction("swnw") == "w"
    assert reduce_direction("sene") == "e"


if __name__ == "__main__":
    main()
