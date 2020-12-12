import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10
import day11


def main():
    for i in range(1, 12):
        print(f"\n============\nRun day {i}")
        eval(f'day{i}.main()')
        print("============")


if __name__ == "__main__":
    main()
