from utils import timer


def process_line(ln):
    op, val = ln.split()
    val = int(val)

    return op, val


def do_op(data, opid, acc):
    cmd, val = data[opid]
    if cmd == 'jmp':
        return opid + val, acc
    elif cmd == "acc":
        acc += val
        return opid + 1, acc
    else:
        return opid + 1, acc


def recur(data, opid, acc, seen, success=False):
    if opid == len(data):
        return acc, True
    if opid in seen:
        return acc, False
    else:
        seen.add(opid)
        return recur(data, *do_op(data, opid, acc), seen, success)


def solve_day8(data):
    seen = set()
    result, _ = recur(data, 0, 0, seen)
    result2 = part2(data)

    return result, result2


def part2(data):
    for i, op in enumerate(data):
        if op[0] == 'acc':
            continue
        seen = set()
        if op[0] == 'nop':
            data[i] = ('jmp', op[1])
        elif op[0] == 'jmp':
            data[i] = ('nop', op[1])

        result, success = recur(data, 0, 0, seen)
        data[i] = op
        if success:
            print(i, op)
            return result


@timer
def main():
    with open("inputs/day8.txt") as f:
        data = [process_line(ln.strip()) for ln in f]

    print(solve_day8(data))


if __name__ == "__main__":
    main()
