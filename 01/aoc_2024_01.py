def read_input(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f.readlines()]

def fix(lines):
    lists = [[],[]]
    for line in lines:
        ap = line.split()
        for k, bep in enumerate(lists):
            bep.append(int(ap[k]))
    return lists

def partone(lists):
    sorted_lists = list(map(sorted, lists))
    return sum(abs(sorted_lists[0][k] - sorted_lists[1][k]) for k in range(len(sorted_lists[0])))

def parttwo(lists):
    return sum(no * lists[1].count(no) for no in lists[0])

lists = fix(read_input("input.txt"))
print(partone(lists))
print(parttwo(lists))
      