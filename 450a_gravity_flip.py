from sys import stdin, stdout


def print(_) -> None:
    stdout.write(str(_) + "\n")


def input() -> str:
    return stdin.readline().strip()


def main() -> None:
    _ = int(input())
    cubes = [int(x) for x in input().split()]
    for i in range(len(cubes)):
        for j in range(len(cubes)):
            if cubes[i] < cubes[j]:
                temp = cubes[i]
                cubes[i] = cubes[j]
                cubes[j] = temp

    print(" ".join([str(cube) for cube in cubes]))


if __name__ == "__main__":
    main()
