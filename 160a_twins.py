from sys import stdin, stdout


def print(_) -> None:
    stdout.write(str(_) + "\n")


def input() -> str:
    return stdin.readline().strip()


def main() -> None:
    n = int(input())
    coins = [int(x) for x in input().split()]
    coins.sort(reverse=True)
    for i in range(n):
        if sum(coins[: i + 1]) > sum(coins[i + 1 :]):
            n = len(coins[: i + 1])
            break
    print(n)


if __name__ == "__main__":
    main()
