from utils import timer


@timer
def main():
    with open("inputs/day25.txt") as f:
        data = [int(ln.strip()) for ln in f]

    print(solve_day25(data))


@timer
def solve_day25(data):
    return part1(data)


@timer
def part1(data):
    cardpk, doorpk = data
    card_secret_loopsize = get_secret_loopsize(cardpk)
    encrypt1 = transform_subjectnumber(doorpk, card_secret_loopsize)

    # door_secret_loopsize = get_secret_loopsize(doorpk)
    # encrypt2 = transform_subjectnumber(cardpk, door_secret_loopsize)
    # assert encrypt1 == encrypt2

    return encrypt1


def one_loop(value, subject_number, divisor=20201227):
    return (value * subject_number) % divisor


def transform_subjectnumber(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value = one_loop(value, subject_number)

    return value


def get_secret_loopsize(public_key):
    value = 1
    count = 0
    while value != public_key:
        value = one_loop(value, 7)
        count += 1

    return count


def test_loop():
    assert transform_subjectnumber(7, 8) == 5764801
    assert transform_subjectnumber(7, 11) == 17807724


def test_get_secret_loopsize():
    assert get_secret_loopsize(5764801) == 8
    assert get_secret_loopsize(17807724) == 11


def test_encryption_key():
    assert transform_subjectnumber(17807724, 8) == 14897079


if __name__ == "__main__":
    main()
