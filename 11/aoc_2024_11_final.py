"""
AoC 2024 Day 11
"""


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def fix(lines):
    return lines[0].split()


cache = {}


def countit(n, stone):
    global cache  # cache used to store already computed values
    if (stone, n) in cache:
        return cache[(stone, n)]
    else:
        if n == 0:
            g = 1
        else:
            L = len(stone)
            if stone == "0":
                g = countit(n - 1, "1")
            elif L % 2:
                g = countit(n - 1, str(int(stone) * 2024))
            else:
                g = countit(n - 1, str(int(stone[: L >> 1]))) + countit(
                    n - 1, str(int(stone[L >> 1 :]))
                )
        cache[(stone, n)] = g
        return g


def partone(data):
    return sum(countit(25, k) for k in data)


def parttwo(data):
    return sum(countit(75, k) for k in data)

from time import process_time
data = fix(read_input("11/input.txt"))
tt = [process_time()]
print(partone(data))
tt.append(process_time())
print(parttwo(data))
tt.append(process_time())
print(tt[1]-tt[0], tt[2]-tt[1])
