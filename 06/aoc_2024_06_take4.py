'''
AoC 2024 Day 6
Take 4
'''

dirmarkers = '^>v<'

def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def annanfix(lines):
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    obstacle_lines = [
        list(filter(lambda n: n != None, [k if c == "#" else None for k,c in enumerate(line)])) for line in lines
    ]
    obstacle_columns = [
        list(filter(lambda n: n != None, [r if line[k] == "#" else None for r, line in enumerate(lines)])) for k in range(len(lines[0]))
        ]  
    for r, line in enumerate(lines):
        for k, c in enumerate(line):
            if c in dirmarkers:
                startpos = (r, k)
                dirnumber = dirmarkers.index(c)
                break
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    return startpos, (obstacle_lines, obstacle_columns), dirs, dirnumber    


def annangrej(pos, obstacles, dirs, dirnumber):
    visited = {pos}
    history = [(pos, dirnumber)]
    while True:
        lastpos = pos
        if dirnumber % 2: # linewise
            line = obstacles[0][pos[0]]
            if dirnumber == 1:
                f = list(filter(lambda x: x != None and x > pos[1], line))
                if f:
                    pos = (pos[0], min(f) - 1)
                    dirnumber += 1
                    dirnumber %= 4 
                    visited.update(set((pos[0], k) for k in range(lastpos[1],pos[1]))) # add all but pos
                else:
                    visited.update(set((pos[0], k) for k in range(pos[1], width)))
                    return {'status':"Out", 'history': history, 'visited': visited}
            if dirnumber == 3:
                f = list(filter(lambda x: x != None and x < pos[1], line))
                if f:
                    pos = (pos[0], max(f) + 1)
                    dirnumber += 1
                    dirnumber %= 4 
                    visited.update(set((pos[0], k) for k in range(lastpos[1],pos[1],-1))) # add all but pos
                else:
                    visited.update(set((pos[0], k) for k in range(pos[1], -1, -1)))
                    return {'status':"Out", 'history': history, 'visited': visited}
        else: # columnwise
            col = obstacles[1][pos[1]]
            if dirnumber == 2:
                f = list(filter(lambda x: x != None and x > pos[0], col))
                if f:
                    pos = (min(f) - 1, pos[1])
                    dirnumber += 1
                    dirnumber %= 4
                    visited.update(set((k, pos[1]) for k in range(lastpos[0],pos[0]))) # add all but pos 
                else:
                    visited.update(set((k, pos[1]) for k in range(pos[0], height)))
                    return {'status':"Out", 'history': history, 'visited': visited}
            if dirnumber == 0:
                f = list(filter(lambda x: x != None and x < pos[0], col))
                if f:
                    pos = (max(f) + 1, pos[1])
                    dirnumber += 1
                    dirnumber %= 4 
                    visited.update(set((k, pos[1]) for k in range(lastpos[0],pos[0],-1))) # add all but pos 
                else:
                    visited.update(set((k, pos[1]) for k in range(pos[0], -1, -1)))                    
                    return {'status':"Out", 'history': history, 'visited': visited}
        if (pos, dirnumber) in history:
            return {'status':"Loop", 'history': history, 'visited': visited}
        else:
            history.append((pos, dirnumber))

def andragrej(pos, obstacles, dirs, dirnumber):
    history = [(pos, dirnumber)]
    while True:
        lastpos = pos
        if dirnumber % 2: # linewise
            line = obstacles[0][pos[0]]
            if dirnumber == 1:
                f = list(filter(lambda x: x != None and x > pos[1], line))
                if f:
                    pos = (pos[0], min(f) - 1)
                    dirnumber += 1
                    dirnumber %= 4 
                else:
                    return {'status':"Out", 'history': history}
            if dirnumber == 3:
                f = list(filter(lambda x: x != None and x < pos[1], line))
                if f:
                    pos = (pos[0], max(f) + 1)
                    dirnumber += 1
                    dirnumber %= 4 
                else:
                    return {'status':"Out", 'history': history}
        else: # columnwise
            col = obstacles[1][pos[1]]
            if dirnumber == 2:
                f = list(filter(lambda x: x != None and x > pos[0], col))
                if f:
                    pos = (min(f) - 1, pos[1])
                    dirnumber += 1
                    dirnumber %= 4
                else:
                    return {'status':"Out", 'history': history}
            if dirnumber == 0:
                f = list(filter(lambda x: x != None and x < pos[0], col))
                if f:
                    pos = (max(f) + 1, pos[1])
                    dirnumber += 1
                    dirnumber %= 4 
                else:
                    return {'status':"Out", 'history': history}
        if (pos, dirnumber) in history:
            return {'status':"Loop", 'history': history}
        else:
            history.append((pos, dirnumber))

lines = read_input('06/input.txt')
pos, obstacles, dirs, dirnumber = annanfix(lines)
height, width = len(lines), len(lines[0])


g = annangrej(pos, obstacles, dirs, dirnumber)

print(len(g['visited']))

s = 0
ap = g['visited']
for (r,c) in ap:
    if c not in obstacles[0][r] and (r,c) != pos:
        ol, oc =  obstacles[0][r].copy(), obstacles[1][c].copy()
        obstacles[0][r].append(c)
        obstacles[1][c].append(r)
        g = andragrej(pos, obstacles, dirs, dirnumber) 
        if g['status'] == "Loop":
            s += 1
        obstacles[0][r], obstacles[1][c] = ol, oc                
print(s)
