'''
AoC 2024 Day 10
'''
import time 

def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

class Pos:
    def __init__(self, coords, height, neighbours = [], pathto = []):
        self.coords, self.height, self.neighbours, self.pathto = coords, height, neighbours, pathto

def fix(lines):
    return [[int(c) for c in line] for line in lines]

def part(data):
    topomap = []
    for r, line in enumerate(data):
        topomap.append([Pos((r,c), v) for c, v in enumerate(line)])
    for r, line in enumerate(topomap):
        for c, p in enumerate(line):
            if r == 0:
                if c == 0:
                    n = [(0,1),(1,0)]
                elif c == len(line) - 1:
                    n = [(0,c-1), (1,c)]
                else:
                    n = [(0,c-1), (0, c+1), (1,c)]
            elif r == len(data) - 1:
                if c == 0:
                    n = [(r,1),(r-1,0)]
                elif c == len(line) - 1:
                    n = [(r,c-1), (r-1,c)]
                else:
                    n = [(r,c-1), (r, c+1), (r-1,c)]
            else:
                if c == 0:
                    n = [(r,1),(r-1,0),(r+1,0)]
                elif c == len(line) - 1:
                    n = [(r,c-1), (r-1,c), (r+1,c)]
                else:
                    n = [(r,c-1), (r, c+1), (r-1,c), (r+1,c)]
            p.neighbours = [topomap[r][c] for (r,c) in n]
            p.pathto = []
    for r in topomap:
        for p in r:
            for n in p.neighbours:
                if n.height == p.height + 1:
                    p.pathto.append(n)
    ssum = 0
    rsum = 0
    for r in topomap:
        for p in r:
            n = {p}
            nn = {(p,)}
            for h in range(9):
                n = set(r for q in n  for r in q.pathto)
                nn = set( pp + (r,) for pp in nn for r in pp[-1].pathto)
            p.score = len(n)
            p.rating = len(nn)
            ssum += p.score
            rsum += p.rating
    return ssum, rsum

t = time.process_time()
data = fix(read_input('10/input.txt'))
print(part(data))
print(time.process_time()-t)