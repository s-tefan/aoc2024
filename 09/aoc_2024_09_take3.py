"""
AoC 2024 Day 9
Take 3, inte funkis än
"""
import time


def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

class Lucka:
    pass

class Fil:
    pass

def fix(lines):
    indata = [int(c) for c in lines[0]]
    no_ids = (len(indata) + 1)//2
    lucklist, fillist = [], []
    pos = 0§
    for k, b in enumerate(indata)
        if k % 2:
            lucka = Lucka()
            lucka.pos = pos
            lucka.len = b
            lucklist.append(lucka)
            pos += b 
        else:
            fil = Fil()
            fil.pos = pos
            fil.len = b
            fil.id = k
            fillist.append(fil)
            pos += b



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