'''
AoC 2024 Day 11
including less functional attempts
'''
def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def fix(lines):
    return lines[0].split()

def replace(stone):
    L = len(stone)
    if L % 2:
        if stone == '0':
            return '1',
        else:
            return str(int(stone)*2024),
    else:
        H = L>>1
        return str(int(stone[:H])), str(int(stone[H:]))

cache = {}

def countit(n, stone):
    global cache # cache used to store already computed values
    if (stone, n) in cache:
        return cache[(stone,n)]
    else:
        if n == 0:
            g = 1
        else:
            L = len(stone)
            if stone == '0':
                g = countit(n - 1, '1')
            elif L % 2:
                g = countit(n - 1, str(int(stone)*2024))
            else:
                g = countit(n - 1, str(int(stone[:L>>1]))) + countit(n-1, str(int(stone[L>>1:])))
        cache[(stone, n)] = g
        return g


def countit1(n, stone):
    # Worked for part one but took too much time for part two
    if n == 0:
        return 1
    else:
        L = len(stone)
        if stone == '0':
            return countit1(n - 1, '1')
        elif L % 2:
            return countit1(n - 1, str(int(stone)*2024))
        else:
            return countit1(n - 1, str(int(stone[:L>>1]))) + countit1(n-1, str(int(stone[L>>1:])))



def blink(stonelist):
    newlist = []
    for stone in stonelist:
        newlist.extend(replace(stone))
    return newlist

def partone(data):
    ''' Worked for part one but took far to much time and memory for part two
    for m in range(25):
        data = blink(data)
    return len(data)
    '''
    return(sum(countit(25, k) for k in data))

    

def parttwo(data): 
    return(sum(countit(75, k) for k in data))



data = fix(read_input('11/input.txt'))
print(partone(data))
data = fix(read_input('11/input.txt'))
print(parttwo(data))