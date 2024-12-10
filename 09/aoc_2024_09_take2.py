"""
AoC 2024 Day 9
Take 2, inte funkis
"""
import time


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]


def fix(lines):
    return lines[0]

def parttwo(line):
    blocks = [int(c) for c in line]
    ids = list(range(len(blocks)+1))
    head = blocks
    tail = []
    for m in range(len(blocks),0,-1):
        a = head.pop()
        b = head.pop()
        breaker = False
        for k, e in enumerate(head[1::2]):
            if a <= e:
                head.insert(k, e - a)
                head.insert(k, a)
                head.insert(k, 0)
                breaker = True
                id = ids.pop(len(head))
                ids.insert(k + 1, id)
                break
        if not breaker:
            tail.insert(0, a)
            tail.insert(0, b)
        print(head, tail)

tt = [time.process_time()]
print(parttwo(fix(read_input('09/test.txt'))))
tt.append(time.process_time())
print([tt[k+1]-tt[k] for k in range(len(tt)-1)])