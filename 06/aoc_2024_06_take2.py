'''
AoC 2024 Day 6
Take 2
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



def move(pos, dir):
    return tuple((pos[k]+dir[k]) for k in range(len(pos)))

    

def grej(pos, obstacles, dirs, dirnumber):
    visited = {pos}
    history = set()
    while True:
        filters = [
            lambda p: p[1] == pos[1] and p[0] < pos[0],
            lambda p: p[0] == pos[0] and p[1] > pos[1],
            lambda p: p[1] == pos[1] and p[0] > pos[0],
            lambda p: p[0] == pos[0] and p[1] < pos[1]
        ]
        keys = [
            lambda p: -p[0],
            lambda p: p[1],
            lambda p: p[0],
            lambda p: -p[1]
        ]
        obsts = list(filter(filters[dirnumber], obstacles))
        if obsts: # There is at least one obstacle in the travelling distance
            next_obst = min(obsts, key = keys[dirnumber])
            d = dirs[dirnumber]
            newpos = tuple(next_obst[k] - d[k] for k in (0,1))
            #print(pos, d, next_obst, newpos, history)

            if (newpos, dirnumber) in history: # newpos och direction _to_ there
                print("LOOP!")
                return "Loop"
            steps = max(abs(pos[0]-newpos[0]), abs(pos[1]-newpos[1]))
            pos = newpos
            visited.update({(pos[0]-k*d[0],pos[1]-k*d[1]) for k in range(steps)})
            history.add((pos, dirnumber))
            dirnumber += 1
            dirnumber %= 4
        else:
            if dirnumber == 0:
                visited.update({(r,pos[1]) for r in range(pos[0])})
            elif dirnumber == 1:
                visited.update({(pos[0], c) for c in range(pos[1]+1, width)})
            elif dirnumber == 2:
                visited.update({(r, pos[1]) for r in range(pos[0]+1, height)})
            elif dirnumber == 3:
                visited.update({(pos[0], c) for c in range(pos[1])})
            return len(visited)

lines = read_input('06/input.txt')
pos, obstacles, dirs, dirnumber = fix(lines)
height, width = len(lines), len(lines[0])


print(grej(pos, obstacles, dirs, dirnumber))


s = 0
for r in range(height):
    for c in range(width):
        print(r,c)
        if (r,c) not in obstacles | {pos}:
            if grej(pos, obstacles | {(r,c)}, dirs, dirnumber) == "Loop":
                s += 1
                
print(s)
