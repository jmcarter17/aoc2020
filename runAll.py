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
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20
import day21
import day22
import day23
import day24
import day25


def main():
    for i in range(1, 26):
        print(f"\n============\nRun day {i}")
        eval(f'day{i}.main()')
        print("============")


if __name__ == "__main__":
    main()
