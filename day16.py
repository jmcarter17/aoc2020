from copy import copy
from math import prod

from utils import timer


@timer
def main():
    with open("inputs/day16.txt") as f:
        data = [x.strip() for x in f]

    idx_end_fields = data.index("")
    fields = {}
    for d in data[0:idx_end_fields]:
        k, nums = d.split(": ")
        fields[k] = [
            range(int(num.split("-")[0]), int(num.split("-")[1]) + 1)
            for num in nums.split(" or ")
        ]

    my_ticket = [int(x) for x in data[idx_end_fields + 2].split(",")]
    other_tickets = [[int(x) for x in d.split(",")] for d in data[idx_end_fields+5:]]

    print(solve_day16(fields, my_ticket, other_tickets))


@timer
def solve_day16(fields, my_ticket, other_tickets):
    result1, other_tickets = part1(fields, other_tickets)
    result2 = part2(fields, my_ticket, other_tickets)

    return result1, result2


@timer
def part1(fields, other_tickets):
    invalid_vals = []
    invalid_tickets_idx = set()
    for i, ticket in enumerate(other_tickets):
        for num in ticket:
            if not check_num(num, fields):
                invalid_vals.append(num)
                invalid_tickets_idx.add(i)

    other_tickets = [val for i, val in enumerate(other_tickets) if i not in invalid_tickets_idx]

    return sum(invalid_vals), other_tickets


def check_num(num, fields):
    return any(num in rg for lst in fields.values() for rg in lst)


@timer
def part2(fields, my_ticket, other_tickets):
    other_tickets.append(my_ticket)
    fieldset = set(fields.keys())
    correct_field = [copy(fieldset) for _ in my_ticket]
    for ticket in other_tickets:
        for i, val in enumerate(ticket):
            potential = set()
            for k, v in fields.items():
                if val in v[0] or val in v[1]:
                    potential.add(k)
            correct_field[i] &= potential

    already_seen = []
    while not all_sizeone(correct_field):
        idx, val = find_new_correct(correct_field, already_seen)
        already_seen.append(idx)
        for i, f in enumerate(correct_field):
            if i != idx:
                correct_field[i] = f - correct_field[idx]

    print(correct_field)

    return prod(my_ticket[i] for i, f in enumerate(correct_field) if "departure" in list(f)[0])


def all_sizeone(correct_fields):
    return all(len(f) == 1 for f in correct_fields)


def find_new_correct(correct_fields, already_seen):
    for i, f in enumerate(correct_fields):
        if len(f) == 1 and i not in already_seen:
            return i, f


if __name__ == "__main__":
    main()
