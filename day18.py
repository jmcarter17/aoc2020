from utils import timer


@timer
def main():
    with open("inputs/day18.txt") as f:
        data = [ln.strip() for ln in f]

    print(solve_day18(data))


@timer
def solve_day18(data):
    result1 = part1(data)
    result2 = part2(data)

    return result1, result2


@timer
def part1(data):
    return sum(execute(expr) for expr in data)


@timer
def part2(data):
    return sum(execute2(expr) for expr in data)


def execute(expr):
    while has_parens(expr):
        expr = exec_parens(expr, execute)

    return exec_left_to_right(expr)


def execute2(expr):
    while has_parens(expr):
        expr = exec_parens(expr, execute2)

    expr = exec_pluses(expr)
    return eval(expr)


def has_parens(expr):
    return expr.find("(") != -1


def exec_parens(expr, fn):
    parens_idx = []
    count = 0
    for i, c in enumerate(expr):
        if c == "(":
            count += 1
            if count == 1:
                parens_idx.append(i)
        elif c == ")":
            count -= 1
            if count == 0:
                parens_idx.append(i)
                break

    return expr.replace(
        expr[parens_idx[0] : parens_idx[1] + 1],
        str(fn(expr[parens_idx[0] + 1 : parens_idx[1]])),
    )


def exec_left_to_right(expr):
    tokens = expr.split()
    binexpr = []
    result = "0"
    for t in tokens:
        binexpr.append(t)
        if len(binexpr) == 3:
            result = str(eval_tokens(binexpr))
            binexpr = [result]

    return int(result)


def exec_pluses(expr):
    tokens = expr.split()
    while "+" in tokens:
        idx = tokens.index("+")
        binexpr = tokens[idx - 1: idx + 2]
        tokens = tokens[: idx - 1] + [str(eval_tokens(binexpr))] + tokens[idx + 2:]

    return " ".join(tokens)


def eval_tokens(expr):
    return eval(" ".join(expr))


if __name__ == "__main__":
    main()
