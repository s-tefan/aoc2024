'''
AoC 2024 Day 8
'''
from math import ceil
import time

def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def fix(lines):
    antennas = {}
    #freqs = set(''.join(lines)).discard('.')
    for r, line in enumerate(lines):
        for k, c in enumerate(line):
            if c != '.':
                if c in antennas:
                    antennas[c].append((r,k))
                else:
                    antennas[c] = [(r,k)]
    return {'antennas': antennas, 'width': len(lines[0]), 'height': len(lines)}

def tdiff(a,b):
    return tuple(map(lambda c: c[0] - c[1], zip(a,b)))

def tmult(k,a):
    return tuple(map(lambda x: k*x, a))

def gcd(a,b):
    r = a % b
    return gcd(b, r) if r else b
    
def partone(data):
    antennas = data['antennas']
    height, width = data['height'], data['width'] 
    antinodes = set()
    for freq in antennas:
        for k, a in enumerate(antennas[freq]):
            for b in antennas[freq][k+1:]:
                for c in [tdiff(tmult(2,a),b), tdiff(tmult(2,b),a)]:
                    if 0 <= c[0] < height and 0 <= c[1] < width:
                        antinodes.add(c)
    return len(antinodes)

def parttwo(data):
    antennas = data['antennas']
    height, width = data['height'], data['width'] 
    antinodes = set()
    for freq in antennas:
        for k, a in enumerate(antennas[freq]):
            for b in antennas[freq][k+1:]:
                a0, a1 = a
                b0, b1 = b
                g = gcd(abs(b1-a1), abs(b0-a0))
                d0, d1 = (b0-a0)//g, (b1-a1)//g
                nstart = max(-(a0//d0) if d0 >= 0 else (height-a0-1)//d0, -(a1//d1) if d1 >= 0 else -((width-a1-1)//-d1) )
                nfinish = min((a0//-d0) if d0 < 0 else (height-a0-1)//d0, a1//-d1 if d1 < 0 else (width-a1-1)//d1)
                for n in range(nstart, nfinish + 1):
                    c = (a0 + n*d0, a1 + n*d1)
                    antinodes.add(c)
    return len(antinodes)
ts = time.perf_counter()
data = fix(read_input('08/input.txt'))
t0 = time.perf_counter()
print(partone(data))
t1 = time.perf_counter()
print(parttwo(data))
t2 = time.perf_counter()
print(t0 - ts, t1 - t0, t2 - t1)