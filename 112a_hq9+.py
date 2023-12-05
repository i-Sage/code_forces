from sys import stdin, stdout


def print(_) -> None:
    stdout.write(str(_) + "\n")


def input() -> str:
    return stdin.readline().strip()


def main() -> None:
    in_str = input()
    hq9plus_keywords = ["H", "Q", "9"]
    for char in in_str:
        if (char.isupper() and char in hq9plus_keywords) or char == "9":
            print("YES")
            return

    print("NO")


if __name__ == "__main__":
    main()
