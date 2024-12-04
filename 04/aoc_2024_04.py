'''
AoC 2024 Day 4
Assuming the text is square
'''

def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def fix(lines):
    return lines


def partone(text):
    n = len(text) # Assuming square block of text
    print(len(text), len(text[0]))
    s = 0
    for line in text:
        for k in range(n-3):
            if line[k:k+4] in {'XMAS', 'SAMX'}:
                s += 1
    for c in range(n):
        for r in range(n-3):
            if ''.join(text[r+k][c] for k in range(4)) in {'XMAS','SAMX'}:
                s += 1
        if n - c >= 4:
            for r in range(n-3):
                if ''.join(text[r+k][c+k] for k in range(4)) in {'XMAS','SAMX'}:
                    s += 1
                if ''.join(text[r+k][(c+3-k)] for k in range(4)) in {'XMAS','SAMX'}:
                    s += 1
    return(s)

    

def parttwo(text):
    n = len(text) # Assuming square
    s = 0
    for r in range(1, n-1):
        for c in range(1, n-1):
            if ''.join(text[r-1+k][c-1+k] for k in range(3)) in {'MAS','SAM'} \
                and ''.join(text[r-1+k][c+1-k] for k in range(3)) in {'MAS','SAM'}:
                s += 1
    return(s)


text = fix(read_input('04/input.txt'))
print(partone(text))
print(parttwo(text))