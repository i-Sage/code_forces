from sys import stdin, stdout


class TestVector(object):
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, value) -> bool:
        return self.x == value.x and self.y == value.y and self.z == value.z


vec1 = TestVector(2, 2, 2)
vec2 = TestVector(2, 2, 2)
print(vec1 == vec2)


def print(_) -> None:
    stdout.write(str(_) + "\n")


def input() -> str:
    return stdin.readline().strip()


def main() -> None:
    input_str = input().split("+")
    input_str.sort()
    print("+".join(input_str))


if __name__ == "__main__":
    main()
