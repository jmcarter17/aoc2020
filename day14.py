from collections import defaultdict

from utils import timer


@timer
def main():
    with open("inputs/day14.txt") as f:
        data = [ln.strip() for ln in f]

    print(solve_day14(data))


@timer
def solve_day14(data):
    result1 = part1(data)
    result2 = part2(data)

    return result1, result2


@timer
def part1(data):
    mems = defaultdict(int)
    maskor = 0
    maskand = 0

    for ln in data:
        if "mask" in ln:
            maskor, maskand = process_mask(ln.split(" = ")[1])
        else:
            mem_idx, val = process_mem(ln)
            val = (val | maskor) & maskand
            mems[mem_idx] = val

    return sum(mems.values())


@timer
def part2(data):
    mems = defaultdict(int)

    for ln in data:
        if "mask" in ln:
            maskstr = ln.split(" = ")[1]
        else:
            mem_idx, val = process_mem(ln)
            for address in get_all_addresses(maskstr, mem_idx):
                mems[address] = val

    return sum(mems.values())


def process_mask(maskstr):
    maskor = int(maskstr.replace("X", "0"), base=2)
    maskand = int(maskstr.replace("X", "1"), base=2)

    return maskor, maskand


def process_mem(ln):
    mem, val = ln.split(" = ")
    mem = int(mem[4:-1])

    return mem, int(val)


def get_all_addresses(maskstr, num):
    num = bin(num)[2:].zfill(36)
    addresses = []
    count = maskstr.count("X")
    new = "".join(
        "{}" if v == "X" else "1" if v == "1" else num[i] for i, v in enumerate(maskstr)
    )
    for n in range(2 ** count):
        n = bin(n)[2:].zfill(count)
        addresses.append(int(new.format(*n), base=2))
    return addresses


if __name__ == "__main__":
    main()
