from sys import stdin, stdout
from math import ceil


def print(_) -> None:
    stdout.write(str(_) + "\n")


def input() -> str:
    return stdin.readline().strip()


def main() -> None:
    m, n = [int(x) for x in input().split()]
    print(int((m * n) / 2))


if __name__ == "__main__":
    main()
