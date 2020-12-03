import day1
import day2
import day3


def main():
    for i in range(1, 4):
        print(f"\n============\nRun day {i}")
        eval(f'day{i}.main()')
        print("============")


if __name__ == "__main__":
    main()
