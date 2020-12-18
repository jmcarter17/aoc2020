from utils import timer


def process_line(ln):
    op, val = ln.split()
    val = int(val)

    return op, val


def do_op(data, pc, acc):
    cmd, val = data[pc]
    if cmd == 'jmp':
        return pc + val, acc
    elif cmd == "acc":
        acc += val
        return pc + 1, acc
    else:
        return pc + 1, acc


def recur(data, pc, acc, seen, success=False):
    if pc == len(data):
        return acc, True
    if pc in seen:
        return acc, False
    else:
        seen.add(pc)
        return recur(data, *do_op(data, pc, acc), seen, success)


def solve_day8(program):
    seen = set()
    result, _ = recur(program, 0, 0, seen)
    result2 = part2(program)

    return result, result2


def part2(program):
    for i, op in enumerate(program):
        if op[0] == 'acc':
            continue
        seen = set()
        if op[0] == 'nop':
            program[i] = ('jmp', op[1])
        elif op[0] == 'jmp':
            program[i] = ('nop', op[1])

        result, success = recur(program, 0, 0, seen)
        program[i] = op
        if success:
            print(i, op)
            return result


@timer
def main():
    with open("inputs/day8.txt") as f:
        program = [process_line(ln.strip()) for ln in f]

    print(solve_day8(program))


if __name__ == "__main__":
    main()
