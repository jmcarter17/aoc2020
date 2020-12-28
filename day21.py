from collections import defaultdict

from utils import timer


@timer
def main():
    data = defaultdict(list)
    ingredients_list = []
    with open("inputs/day21.txt") as f:
        for ln in f:
            openparen = ln.index('(')
            allergens = ln.strip()[openparen + 10:-1].split(", ")
            ingredients = set(ln.strip()[:openparen-1].split(" "))
            for allergen in allergens:
                data[allergen].append(ingredients)
            ingredients_list.append(ingredients)

    print(solve_day21(data, ingredients_list))


@timer
def solve_day21(data, ingredients_list):
    result1, allergens = part1(data, ingredients_list)
    result2 = part2(allergens)

    return result1, result2


@timer
def part1(data, ingredients):
    data = {k: set.intersection(*data[k]) for k in data}
    allergens = {}
    while data != {}:
        shortest = next(k for k, v in data.items() if len(v) == 1 and k not in allergens)
        allergens[shortest] = data[shortest]
        data.pop(shortest)
        for k in data:
            data[k] = data[k] - allergens[shortest]

    bad_ingredients = set.union(*allergens.values())
    count = sum(len(v - bad_ingredients) for v in ingredients)

    return count, allergens


@timer
def part2(allergens):
    return ",".join(allergens[k].pop() for k in sorted(allergens.keys()))


if __name__ == "__main__":
    main()
