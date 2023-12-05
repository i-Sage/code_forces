from sys import stdin, stdout


def print(_) -> None:
    stdout.write(str(_) + "\n")


def input() -> str:
    return stdin.readline().strip()


def main() -> None:
    in_str_1 = input().lower()
    in_str_2 = input().lower()
    if in_str_1 > in_str_2:
        print(1)
    elif in_str_1 == in_str_2:
        print(0)
    else:
        print(-1)

if __name__ == "__main__":
    main()
