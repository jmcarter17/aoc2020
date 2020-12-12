from utils import timer
import numpy as np


DIRECTIONS = {
    "E": np.array((1, 0)),
    "N": np.array((0, 1)),
    "W": np.array((-1, 0)),
    "S": np.array((0, -1)),
}
CWROT = np.array([[0, -1], [1, 0]])
CCWROT = np.array([[0, 1], [-1, 0]])


@timer
def main():
    with open("inputs/day12.txt") as f:
        data = [process_line(ln.strip()) for ln in f]

    print(solve_day12(data))


def process_line(ln):
    action = ln[0]
    number = int(ln[1:])

    return action, number


@timer
def solve_day12(data):
    result1 = part1(data)
    result2 = part2(data)

    return result1, result2


@timer
def part1(data):
    waypoint = DIRECTIONS["E"]
    pos = np.array((0, 0))
    for cmd in data:
        pos, waypoint = do_cmd(cmd, pos, waypoint)

    return sum(abs(pos))


def do_cmd(cmd, pos, waypoint):
    action, val = cmd
    if action in "RL":
        waypoint = change_dir(waypoint, cmd)
    elif action == "F":
        pos += val * waypoint
    else:
        pos += val * DIRECTIONS[action]

    return pos, waypoint


def change_dir(d, cmd):
    if cmd[0] == "R":
        d = rotate(d, CCWROT, (cmd[1] // 90) % 4)
    elif cmd[0] == "L":
        d = rotate(d, CWROT, (cmd[1] // 90) % 4)
    return d


@timer
def part2(data):
    waypoint = np.array([10, 1])
    pos = np.array((0, 0))
    for cmd in data:
        if cmd[0] == "F":
            pos += cmd[1] * waypoint
        else:
            waypoint = update_waypoint(waypoint, cmd)

    return sum(abs(pos))


def update_waypoint(waypoint, cmd):
    if cmd[0] == "R":
        waypoint = rotate(waypoint, CCWROT, (cmd[1] // 90) % 4)
    elif cmd[0] == "L":
        waypoint = rotate(waypoint, CWROT, (cmd[1] // 90) % 4)
    else:
        waypoint += np.array(DIRECTIONS[cmd[0]]) * cmd[1]

    return waypoint


def rotate(vector, rot_matrix, num):
    for _ in range(num):
        vector = rot_matrix.dot(vector)

    return vector


if __name__ == "__main__":
    main()
