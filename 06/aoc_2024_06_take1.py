'''
AoC 2024 Day 6
Take 1
'''

def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def fix(lines):
    obstacles = set()
    dirmarkers = '^>v<'
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    for ln, line in enumerate(lines):
        for cn, c in enumerate(line):
            if c == '#':
                obstacles.add((ln,cn))
            elif c in dirmarkers:
                startpos = (ln,cn)
                dirnumber = dirmarkers.index(c)
    return startpos, obstacles, dirs, dirnumber


'''
def partone(rules, lists):

def parttwo(rules, lists):
'''

def move(pos, dir):
    return tuple((pos[k]+dir[k]) for k in range(len(pos)))

def inside(pos, height, width):
    return 0 <= pos[0] < height and 0 <= pos[1] < width

class Loop(Exception):
    pass
    
lines = read_input('06/input.txt')
pos, obstacles, dirs, dirnumber = fix(lines)
visited = set()
history = set()
height, width = len(lines), len(lines[0])
hlist = []

def grej(pos, obstacles, dirs, dirnumber):
    visited={pos}
    history = set()
    while True:
        newpos = move(pos, dirs[dirnumber])
        if newpos in obstacles:
            dirnumber += 1
            dirnumber %= 4
        else:
            if not inside(newpos, height, width):
                return len(visited)
            pos = newpos
            if (pos, dirnumber) in history:
                raise(Loop)
            visited.add(pos)
            history.add((pos,dirnumber))
            #hlist.append((pos,dirs[dirnumber]))


print(grej(pos, obstacles, dirs, dirnumber))


s = 0
for r in range(height):
    for c in range(width):
        if (r,c) not in obstacles | {pos}:
            try:
                grej(pos, obstacles | {(r,c)}, dirs, dirnumber)
                print(r,c)
            except Loop:
                print(r,c,'Loop')
                s += 1
            except:
                print(r,c,'Dö')
                


print(s)
