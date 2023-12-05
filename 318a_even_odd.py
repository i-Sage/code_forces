from sys import stdin, stdout
from math import ceil


def print(_) -> None:
    stdout.write(str(_) + "\n")


def input() -> str:
    return stdin.readline().strip()


def main() -> None:
    n, k = [int(x) for x in input().split()]
    if k <= ceil(n / 2):
        # if k % 2 != 0:
        print(abs(2 * k - 1))
    else:
        print(abs(2 * k))


if __name__ == "__main__":
    main()
